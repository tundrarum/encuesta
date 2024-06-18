# Encuesta

## Installation

Set up a python virtual environment

    python3 -m venv venv

Install depedencies

    pip3 install -r requirements.txt

## Running it

Load the python virtual environment

    python3 -m venv venv

Run the `ecv.py` script:

```
❯ python3 ecv.py
SELECT * FROM esudb23d LIMIT 5
(2023, 'ES', 1, 'ES21', 1, 771.36261, 1, 2, 1)
(2023, 'ES', 2, 'ES21', 1, 336.92678, 1, 2, 1)
(2023, 'ES', 3, 'ES21', 1, 1205.41445, 1, 2, 1)
(2023, 'ES', 4, 'ES21', 1, 1195.38532, 1, 2, 1)
(2023, 'ES', 5, 'ES21', 1, 1153.82804, 1, 2, 1)

SELECT * FROM TRL010F LIMIT 5
(-2, 'No aplicable (N.A.) (ya que no tiene la edad para ser admitida en estos centros o cursa estudios primarios o tiene más de 12 años) ')
(-1, 'No consta')
(1, 'Variable completada')
```
