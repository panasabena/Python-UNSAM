# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:33:56 2021

Ejercicio 3.11

@author: Alfredo
"""

precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }
#print(precios)
lista_precios = list(zip(precios.values(),precios.keys()))
print(lista_precios)

print('Minimo:','\n',min(lista_precios))
print('Maximo:','\n',max(lista_precios))

print('Se ordena por orden alfabetico:','\n',sorted(lista_precios))
#%%
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]

#%%
import csv
ruta_del_archivo=(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv')
ruta_del_archivo_2=(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion2.csv')
def leer_camion(ruta_del_archivo): ## Le pasamos la ruta del archivo
    
    with open(ruta_del_archivo, 'rt') as f: ## Abre el archivo
        rows = csv.reader(f) ## Lee el archivo
        headers = next(rows) ## Identifica las columnas
        camion = [] ## Creamos una lista vacía
        for row in rows: ## Iteramos en cada fila del archivo
            d = {'Nombre': row[0], ## Creamos un diccionario con cada elemento
                 'Cajones': int(row[1]), ## del archivo que le pasamos
                 'Precio': float(row[2])
            }
            camion.append(d) ## Le agregamos a la lista el diccionario

        total=0.0 ## Creamos una variable flotante en cero         
        for s in camion: ## Para luego iterar en la lista camion
            total +=((s['Cajones']*s['Precio'])) ## Y sumar el precio del cajon
                                                 ## por las frutas   
        #print (total) ## Imprimimos el total
        return camion

## Camion 1
camion = leer_camion(ruta_del_archivo)
from collections import Counter
tenencias=Counter()
for s in camion:
    tenencias[s['Nombre']] += s['Cajones']
#print(tenencias)
## Las 3 frutas con mas cajones:
#print(tenencias.most_common(3))

camion = leer_camion(ruta_del_archivo)
from collections import Counter
tenencias=Counter()
for s in camion:
    tenencias[s['Nombre']] += s['Cajones']

#print(tenencias)
## Las 3 frutas con mas cajones:
#print(tenencias.most_common(3))

## Camion 2>
def leer_camion(ruta_del_archivo_2): ## Le pasamos la ruta del archivo
    
    with open(ruta_del_archivo_2, 'rt') as f: ## Abre el archivo
        rows = csv.reader(f) ## Lee el archivo
        headers = next(rows) ## Identifica las columnas
        camion = [] ## Creamos una lista vacía
        for row in rows: ## Iteramos en cada fila del archivo
            d = {'Nombre': row[0], ## Creamos un diccionario con cada elemento
                 'Cajones': int(row[1]), ## del archivo que le pasamos
                 'Precio': float(row[2])
            }
            camion.append(d) ## Le agregamos a la lista el diccionario

        total=0.0 ## Creamos una variable flotante en cero         
        for s in camion: ## Para luego iterar en la lista camion
            total +=((s['Cajones']*s['Precio'])) ## Y sumar el precio del cajon
                                                 ## por las frutas   
        #print (total) ## Imprimimos el total
        return camion

## Camion 2
camion_2 = leer_camion(ruta_del_archivo_2)
from collections import Counter
tenencias2=Counter()
for s in camion_2:
    tenencias2[s['Nombre']] += s['Cajones']
#print(tenencias2)
## Las 3 frutas con mas cajones:
#print(tenencias2.most_common(3))

camion_2 = leer_camion(ruta_del_archivo_2)
from collections import Counter
tenencias2=Counter()
for s in camion_2:
    tenencias2[s['Nombre']] += s['Cajones']
#print(tenencias2)
## Las 3 frutas con mas cajones:
#print(tenencias2.most_common(3))
combinada= tenencias + tenencias2
print(combinada)