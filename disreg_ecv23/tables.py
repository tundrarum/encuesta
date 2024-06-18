import csv

from glob import glob
from collections import defaultdict

import openpyxl

keys = defaultdict(list)

for file in glob('*.xlsx'):
    wb = openpyxl.load_workbook(file)
    for sheet in wb.worksheets:
        if sheet.title.startswith('Tablas'):

            current_key = None
            in_key = None
            rows = sheet.iter_rows(values_only=True)
            for row in rows:
                f1, f2 = row[:2]
                if not in_key and isinstance(f1, str):
                    current_key = f"{file}/{sheet.title}/{f1}"
                    in_key = True
                    next(rows)
                elif in_key:
                    if f1 is not None:
                        keys[current_key].append((f1,f2))
                    else:
                        in_key = False

with open('tables.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for sheet, rows in keys.items():
        for key, val in rows:
            writer.writerow([sheet,key,val])
