# Encuesta

## Installation

Install [DuckDB CLI](https://duckdb.org/docs/installation/index?version=stable&environment=cli&platform=macos&download_method=package_manager).

## Usage

First unzip the database:

    gunzip -c db/ecv.duckdb.gz > db/ecv.duckdb

Use the `duckdb db/ecv.duckdb` cli to interact with the database. Example

```
❯ duckdb ecv.duckdb
v1.0.0 1f98600c2c
Enter ".help" for usage hints.
D .schema
CREATE TABLE DB040(id VARCHAR, desc VARCHAR);
CREATE TABLE DB040_F(id BIGINT, desc VARCHAR);
CREATE TABLE DB100(id BIGINT, desc VARCHAR);
CREATE TABLE HB050_F(id BIGINT, desc VARCHAR);
CREATE TABLE HC001(id BIGINT, desc VARCHAR);
CREATE TABLE HC002(id BIGINT, desc VARCHAR);
...

D SELECT * FROM esudb23d LIMIT 5;
┌───────┬─────────┬───────┬─────────┬─────────┬────────────┬─────────┬───────┬─────────┐
│ DB010 │  DB020  │ DB030 │  DB040  │ DB040_F │   DB090    │ DB090_F │ DB100 │ DB100_F │
│ int64 │ varchar │ int64 │ varchar │  int64  │   double   │  int64  │ int64 │  int64  │
├───────┼─────────┼───────┼─────────┼─────────┼────────────┼─────────┼───────┼─────────┤
│  2023 │ ES      │     1 │ ES21    │       1 │  771.36261 │       1 │     2 │       1 │
│  2023 │ ES      │     2 │ ES21    │       1 │  336.92678 │       1 │     2 │       1 │
│  2023 │ ES      │     3 │ ES21    │       1 │ 1205.41445 │       1 │     2 │       1 │
│  2023 │ ES      │     4 │ ES21    │       1 │ 1195.38532 │       1 │     2 │       1 │
│  2023 │ ES      │     5 │ ES21    │       1 │ 1153.82804 │       1 │     2 │       1 │
└───────┴─────────┴───────┴─────────┴─────────┴────────────┴─────────┴───────┴─────────┘

D SELECT esudb23d.*, DB100.desc as DB100_desc FROM esudb23d, DB100 WHERE esudb23d.DB100 = DB100.id LIMIT 5;
┌───────┬─────────┬───────┬─────────┬─────────┬────────────┬─────────┬───────┬─────────┬────────────┐
│ DB010 │  DB020  │ DB030 │  DB040  │ DB040_F │   DB090    │ DB090_F │ DB100 │ DB100_F │ DB100_desc │
│ int64 │ varchar │ int64 │ varchar │  int64  │   double   │  int64  │ int64 │  int64  │  varchar   │
├───────┼─────────┼───────┼─────────┼─────────┼────────────┼─────────┼───────┼─────────┼────────────┤
│  2023 │ ES      │     1 │ ES21    │       1 │  771.36261 │       1 │     2 │       1 │ Zona media │
│  2023 │ ES      │     2 │ ES21    │       1 │  336.92678 │       1 │     2 │       1 │ Zona media │
│  2023 │ ES      │     3 │ ES21    │       1 │ 1205.41445 │       1 │     2 │       1 │ Zona media │
│  2023 │ ES      │     4 │ ES21    │       1 │ 1195.38532 │       1 │     2 │       1 │ Zona media │
│  2023 │ ES      │     5 │ ES21    │       1 │ 1153.82804 │       1 │     2 │       1 │ Zona media │
└───────┴─────────┴───────┴─────────┴─────────┴────────────┴─────────┴───────┴─────────┴────────────┘
```

## Building the database

This step is not usually needed as the repository already contains the binary database that can be used as documented in the [Usage](#usage) section.

Set up a python virtual environment

    python3 -m venv venv

Install depedencies

    pip3 install -r requirements.txt

Run `make build`. It will delete (if exists) and then create `db/ecv.duckdb` and the compress it to `db/ecv.duckdb.gz`.
