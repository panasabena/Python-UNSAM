# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 07:28:08 2021

@author: Alfredo
"""
valor = 0
n = 1
s= []
d = {}
## Asignaciones

a = valor # Asignacion a una variable
s[n] = valor # Asignacion a una lista en donde 'n' es la posicion de la lista 
s.append(valor) # asignacion al final de una lista
d['key'] = valor
#%%
types = [str, int, float] # Esta fila convierte a los elementos recorridos
                          # en el tipo de elemento que se le indica
import csv
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next (rows)
print(row)

# Se llama a la lista types[posicion] con su tipo de elemento y luego
# al elemento del archivo que sequiere modificar el tipo de elemento
print(types[1](row[1]))
#%%
types=[str,float,str,str,float,float,float,float,int]
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next (rows)
#print (headers)
#print (row)
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
print(record)
