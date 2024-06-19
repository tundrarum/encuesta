build:
	. venv/bin/activate
	python3 codes.py
	python3 ecv.py
	gzip ecv.duckdb -n -c > ecv.duckdb.gz
