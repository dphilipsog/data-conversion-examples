import csv

with open('fruitcosts.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    print(row)