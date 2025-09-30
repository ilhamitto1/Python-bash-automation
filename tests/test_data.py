import csv
import pytest

def load_rows(path="data/data.csv"):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

def test_csv_not_empty():
    rows = load_rows()
    assert len(rows) > 0

def test_fields_present():
    rows = load_rows()
    for r in rows:
        assert 'id' in r and 'name' in r and 'age' in r

def test_age_valid():
    rows = load_rows()
    for r in rows:
        assert int(r['age']) >= 18
