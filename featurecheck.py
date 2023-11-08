import csv

with open('features.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(f"Data: {row}")
