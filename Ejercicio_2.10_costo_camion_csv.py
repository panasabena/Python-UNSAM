##Costo camion, importando csv
import csv
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Github UNSAM\Programacion_en_Python_UNSAM-master\Notas\ejercicios_python\Data\camion.csv','rt')
rows = csv.reader(f)
headers= next (rows)
#print(headers)
costo=[]
for i in f:
    row = i.split(',')
    a = float(row[1])
    b = float(row[2])
    costo.append(a*b)
print('Costo total: ', sum(costo))
