import csv
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv')
rows = csv.reader(f)
headers = next(rows)
headers
for row in rows:
    print(row)
    
