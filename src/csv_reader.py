import csv

from files import CSV_FILE_PATH

with open(CSV_FILE_PATH, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
