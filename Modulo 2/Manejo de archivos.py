# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:10:38 2022

@author: Alfredo
"""

## Abro el archivo
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Modulo 2\arboles.csv','rt')
## rt hace referencia a r que es read osea de lectura y t de texto. Tambien
## puede ser w que es de escritura, write.
#%%
# imprimo el archivo
data = f.read()
print (data)
#%%
# Cierro el archivo
f.close()
#%%
# Usando el with open no hace falta usar el close():

nombre_archivo = r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Modulo 2\arboles.csv'
with open(nombre_archivo, 'rt') as archivo:
    for i, linea in enumerate (archivo):
        print(i, linea)
        
#%%
f = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Modulo 2\arboles.csv','rt')
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    print(fila)
#%%
## Para abrir un archivo y escribir sobre el:
g = open('bar.txt', 'wt') # Abrir para escritura ('w' de write, 't' de text)
#f= open("guru99.txt","w+")
g.write('un texto')
g.close()
#%%
## Abrimos el archivo anterior
gg = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Modulo 2\bar.txt','rt')
df=gg.read()
print(df)
















