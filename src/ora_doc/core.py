from __future__ import annotations
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Column:
    name:str
    datatype:str
    nullable:bool=True

@dataclass(frozen=True)
class Table:
    name:str
    columns:list[Column]

def _split_top_level(body:str)->list[str]:
    out=[]; buf=[]; depth=0
    for ch in body:
        if ch=="(": depth+=1
        elif ch==")": depth-=1
        if ch=="," and depth==0:
            out.append("".join(buf).strip()); buf=[]
        else:
            buf.append(ch)
    if "".join(buf).strip():
        out.append("".join(buf).strip())
    return out

def parse_tables(sql:str)->list[Table]:
    tables=[]
    for m in re.finditer(r"CREATE\s+TABLE\s+([\w.$#]+)\s*\((.*?)\)\s*;",sql,re.I|re.S):
        name=m.group(1).upper()
        cols=[]
        for item in _split_top_level(m.group(2)):
            if re.match(r"^(CONSTRAINT|PRIMARY|FOREIGN|UNIQUE|CHECK)\b",item,re.I):
                continue
            c=re.match(r'^([\w$#]+)\s+([A-Za-z0-9_]+(?:\s*\([^)]*\))?)(.*)$',item,re.I|re.S)
            if c:
                datatype=re.sub(r"\s+","",c.group(2).upper())
                nullable=not bool(re.search(r"\bNOT\s+NULL\b",c.group(3),re.I))
                cols.append(Column(c.group(1).upper(),datatype,nullable))
        tables.append(Table(name,cols))
    return tables

def render_markdown(tables:list[Table])->str:
    parts=[]
    for t in tables:
        parts += [f"## {t.name}","","| Column | Type | Nullable |","|---|---|---|"]
        parts += [f"| {c.name} | {c.datatype} | {'Yes' if c.nullable else 'No'} |" for c in t.columns]
        parts.append("")
    return "\n".join(parts).rstrip()+"\n"

def render_mermaid(tables:list[Table])->str:
    lines=["erDiagram"]
    for t in tables:
        lines.append(f"    {t.name.replace('.','_')} {{")
        for c in t.columns:
            dtype=c.datatype.replace("(","_").replace(")","").replace(",","_")
            lines.append(f"        {dtype} {c.name}")
        lines.append("    }")
    return "\n".join(lines)
