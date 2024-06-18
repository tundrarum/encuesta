import duckdb

TABLES = {
    "esudb23d": "./data/ECV_Td_2023/CSV/esudb23d.csv",
    "esudb23h": "./data/ECV_Th_2023/CSV/esudb23h.csv",
    "esudb23p": "./data/ECV_Tp_2023/CSV/esudb23p.csv",
    "esudb23r": "./data/ECV_Tr_2023/CSV/esudb23r.csv",
}

con = duckdb.connect(database = ":memory:")

for tbl, path in TABLES.items():
    con.execute(f"CREATE TABLE {tbl} AS SELECT * FROM read_csv('{path}')")

result = con.execute("SELECT * FROM esudb23d LIMIT 5").fetchall()
for row in result:
    print(row)

# output:
# (2023, 'ES', 1, 'ES21', 1, 771.36261, 1, 2, 1)
# (2023, 'ES', 2, 'ES21', 1, 336.92678, 1, 2, 1)
# (2023, 'ES', 3, 'ES21', 1, 1205.41445, 1, 2, 1)
# (2023, 'ES', 4, 'ES21', 1, 1195.38532, 1, 2, 1)
# (2023, 'ES', 5, 'ES21', 1, 1153.82804, 1, 2, 1)
