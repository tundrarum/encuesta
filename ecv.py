import os

from glob import glob

import duckdb

DB_NAME = "ecv.duckdb"

try:
    os.remove(DB_NAME)
except OSError:
    pass

con = duckdb.connect(database=DB_NAME)

# READ csv's
for csv_path in glob("data/**/*.csv", recursive=True):
    for path in glob(csv_path):
        tbl = os.path.splitext(os.path.basename(path))[0]
        con.execute(f"CREATE TABLE {tbl} AS SELECT * FROM read_csv('{path}')")
