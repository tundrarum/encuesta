build:
	. venv/bin/activate
	python3 ecv.py
	gzip db/ecv.duckdb -n -c > db/ecv.duckdb.gz
