from __future__ import annotations
import argparse
from pathlib import Path
from .core import parse_tables,render_markdown,render_mermaid

def main(argv=None):
    p=argparse.ArgumentParser(description="Generate docs from Oracle DDL.")
    p.add_argument("source")
    p.add_argument("--format",choices=("markdown","mermaid"),default="markdown")
    a=p.parse_args(argv)
    tables=parse_tables(Path(a.source).read_text(encoding="utf-8"))
    print(render_markdown(tables) if a.format=="markdown" else render_mermaid(tables))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
