# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 01:51:09 2021

Ejercicio: Tabla_informe

@author: Alfredo
"""



#%%
import csv
ruta_del_archivo = (r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv')
def leer_camion(ruta_del_archivo): ## Le pasamos la ruta del archivo
    
    with open(ruta_del_archivo, 'rt') as f: ## Abre el archivo
        rows = csv.reader(f) ## Lee el archivo
        headers = next(rows) ## Identifica las columnas
        camion = [] ## Creamos una lista vacía
        cambio = [8.02,15.18,2.02,29.66,33.11,15.79,35.84]
        for row,c in zip(rows,cambio): ## Iteramos en cada fila del archivo
            d = {'Nombre': row[0], ## Creamos un diccionario con cada elemento
                 'Cajones': int(row[1]), ## del archivo que le pasamos
                 'Precio': float(row[2]),
                 'Cambio': float(c)
            }
            camion.append(d) ## Le agregamos a la lista el diccionario

        total=0.0 ## Creamos una variable flotante en cero         
        #for c in cambio: ## Para luego iterar en la lista camion
         #   cambio['Cambio']==c ## Y sumar el precio del cajon
            #camion.append(j)## por las frutas   
        #print (total) ## Imprimimos el total
        
        return camion

## Código de stackoverflow
def printTable(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = '  '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))
