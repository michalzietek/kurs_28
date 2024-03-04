import csv


with open("dane.csv") as plik:
    reader = csv.reader(plik)
    for row in reader:
        print(row)