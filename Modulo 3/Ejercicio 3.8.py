# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 01:36:57 2021

@author: Alfredo
"""

#%%
for n in range(10):
    print(n, end=' ')

#%%
for n in range(10,0,-1):
    print(n, end=' ')
#%%
for n in range(0,10,2):
    print(n, end=' ')
#%%
#Ejercicio 3.7
data = [4, 9, 1, 25, 16, 100, 49]
print(min(data))
print(max(data))
print(sum(data))
# Para iterar en los datos
for x in data:
        print(x)
#%%
data = [4, 9, 1, 25, 16, 100, 49]
for n,x in enumerate(data):
    print(n,x)
#%%
# Ejercicio 3.8
import csv
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Github UNSAM\Programacion_en_Python_UNSAM-master\Notas\ejercicios_python\Data\missing.csv','rt')
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
#%%
## Creando funcion con salvedad de errores:
ruta_del_archivo=r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Github UNSAM\Programacion_en_Python_UNSAM-master\Notas\ejercicios_python\Data\missing.csv'
def costo_camion(ruta_del_archivo):
    f = open(ruta_del_archivo,'rt')
    headers = next(f).split(',')
    #print(headers)
    costo=[]
    for i in f:
        #print(i)
        try:
            for n,i in enumerate(f,start=2):
                row = i.split(',')
                #if row[1] != '':
                    
                a = float(row[1])
                b = float(row[2])
                costo.append(a*b)
            for i in f:
                row = i.split(',')
                if i=='':
                    costo.append(0)               
            return sum(costo)
    
        except ValueError:
            print ("Fila",n,':',"No se puede interpretar",i)
        
