# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:29:22 2021

@author: Alfredo
"""


## fileparse ejercicio 6.6
import csv

def parse_csv(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open (nombre_archivo) as f:
        rows = csv.reader(f)
        # Headers lee los encabezados
        headers = next(rows)
        registros = []
        
        for row in rows:
            if not row: # saltea las filas sin datos
                continue
            registro = dict(zip(headers,row))
            registros.append(registro)
    return registros
camion=parse_csv(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv')
print(camion)
#%%
precios = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\precios.csv') 
csvreader = csv.reader(precios)
header = []
header = next(csvreader)
rows=[]
for row in csvreader:
    rows.append(row)   
precios.close()
#%%
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\precios.csv')
for linea in f:
    print(linea)
f.close()
#%%
def parse(nombre_archivo,select=None):
    csvreader = csv.reader(nombre_archivo)
    header = []
    header = next(csvreader)
    rows = []
    for r,j in enumerate(csvreader):
        row=(r,j)
        print (row)
#%%
precios = parse_csv(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\precios.csv', types=[str,float], has_headers=False)

#%%
encabezados = ['nombre','dia', 'hora', 'cajones', 'precio']
select = ['nombre', 'cajones']
indices = [encabezados.index(nombre_columna) for nombre_columna in select]
print (indices)
#%%
