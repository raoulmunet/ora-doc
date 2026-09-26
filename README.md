# ora-doc

[![tests](https://github.com/raoulmunet/ora-doc/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-doc/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

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

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
