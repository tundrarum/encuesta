build:
	. venv/bin/activate
	python3 ecv.py
	gzip ecv.duckdb -c > ecv.duckdb.gz
