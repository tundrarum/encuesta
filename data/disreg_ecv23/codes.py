import csv
import os
import shutil


from glob import glob
from collections import defaultdict

import openpyxl

CODE_DIR = "codes"

shutil.rmtree(CODE_DIR, ignore_errors=True)
os.mkdir(CODE_DIR)

keys = defaultdict(list)

for file in glob('*.xlsx'):
    wb = openpyxl.load_workbook(file)
    for sheet in wb.worksheets:
        if sheet.title.startswith('Tablas'):
            code = None
            in_key = None
            rows = sheet.iter_rows(values_only=True)
            for row in rows:
                f1, f2, f3 = row[:3]

                try:
                    f3 = f3.split()[0]
                except AttributeError:
                    pass

                if not in_key and isinstance(f1, str):
                    code = f3
                    in_key = True
                    next(rows)
                elif in_key:
                    if f1 is not None:
                        keys[code].append((f1,f2))
                    else:
                        in_key = False

# Write CSVs
for code, rows in keys.items():
    with open(f'{CODE_DIR}/{code}.csv', 'w') as codefile:
        code_writer = csv.writer(codefile)
        code_writer.writerow(["id", "description"])
        for key, val in rows:
            code_writer.writerow([key, val])
