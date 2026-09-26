# ora-doc

Generate compact Markdown documentation from Oracle DDL.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Supported for common CREATE TABLE / constraint syntax |
> | Oracle Database 23ai | ✅ Supported for common CREATE TABLE / constraint syntax |
> | Oracle AI Database 26ai | ✅ Supported for common CREATE TABLE / constraint syntax |
>
> Version-specific DDL clauses outside the supported grammar are preserved as unsupported text rather than misdocumented.

## Features

- parse common `CREATE TABLE` statements;
- document columns, datatypes and nullability;
- recognize inline/table-level primary and foreign keys;
- produce Markdown tables;
- generate a Mermaid ER sketch for detected foreign keys;
- offline and credential-free.

## Installation

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-doc.git"
```

## Usage

```bash
ora-doc examples/schema.sql > SCHEMA.md
ora-doc examples/schema.sql --format mermaid > schema.mmd
```

## Example output

```markdown
## DWH.CUSTOMER_DIM

| Column | Type | Nullable |
|---|---|---|
| CUSTOMER_ID | NUMBER | No |
| CUSTOMER_NAME | VARCHAR2(200) | Yes |
```

## Limitations

This is a documentation generator, not a replacement for Oracle's complete SQL grammar. Advanced object types, nested tables, object-relational syntax and metadata-only properties will be added incrementally and documented by version where relevant.

## License

MIT.
