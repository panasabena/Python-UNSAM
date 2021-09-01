import csv
from collections import Counter
def leer_parque(nombre_archivo, parque):
    lista=[]
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            registro = dict(zip(encabezados, fila))
            if registro['espacio_ve'] == parque :
                lista.append(registro)
    return lista
gral_paz = leer_parque(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')    
len(gral_paz )
