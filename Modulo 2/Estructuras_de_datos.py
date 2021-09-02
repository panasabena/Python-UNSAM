import csv
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv')
filas = csv.reader(f)
next(filas)
fila = next(filas)
fila
d = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }
print(d)
