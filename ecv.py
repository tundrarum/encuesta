import os

from glob import glob

import duckdb


PATHS = [
    "./data/disreg_ecv23/codigos/*.csv",
    "./data/*/CSV/*.csv",
]

con = duckdb.connect(database=":memory:")

# READ csv's
for csv_path in PATHS:
    for path in glob(csv_path):
        tbl = os.path.splitext(os.path.basename(path))[0]
        con.execute(f"CREATE TABLE {tbl} AS SELECT * FROM read_csv('{path}')")

# Example queries
sqls = [
    "SELECT * FROM esudb23d LIMIT 5",
    "SELECT * FROM TRL010F LIMIT 5",
]
for sql in sqls:
    print(sql)
    result = con.execute(sql).fetchall()
    for row in result:
        print(row)
    print()

# output:
# ❯ python3 ecv.py
# SELECT * FROM esudb23d LIMIT 5
# (2023, 'ES', 1, 'ES21', 1, 771.36261, 1, 2, 1)
# (2023, 'ES', 2, 'ES21', 1, 336.92678, 1, 2, 1)
# (2023, 'ES', 3, 'ES21', 1, 1205.41445, 1, 2, 1)
# (2023, 'ES', 4, 'ES21', 1, 1195.38532, 1, 2, 1)
# (2023, 'ES', 5, 'ES21', 1, 1153.82804, 1, 2, 1)
#
# SELECT * FROM TRL010F LIMIT 5
# (-2, 'No aplicable (N.A.) (ya que no tiene la edad para ser admitida en estos centros o cursa estudios primarios o tiene más de 12 años) ')
# (-1, 'No consta')
# (1, 'Variable completada')
