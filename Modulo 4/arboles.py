# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:18:28 2021

@author: Alfredo
"""

# arboles.py

  
import csv
from collections import Counter
def leer_parque(nombre_archivo):
    lista=[]
    with open(nombre_archivo, encoding = 'utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            registro = dict(zip(encabezados, fila))
            lista.append(registro)
    return lista
arboleda = leer_parque(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\arbolado-en-espacios-verdes.csv')
#print(arboles)
H=[float(arbol['altura_tot']) for arbol in arboleda]
## ESTA PARTE ES DEL EJERCICIO 4.16

Jacaranda=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
## ESTA PARTE ES DEL EJERCICIO 4.17

diamjac=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

lista_de_tuplas=list(zip(Jacaranda,diamjac))

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

# Ejercicio 4.18 medidas de especies: 
# esta parte no me salió, tampoco renegué mucho.
def medidas_de_especies(especies, arboleda):
    lista=[]
    
    altura=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especies[0]]
    lista.append(dict(altura))
    diametro=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==especies[0]]
    lista.append(dict(diametro))
    altura_1=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especies[1]]
    lista.append(dict(altura_1))
    diametro_1=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==especies[1]]
    lista.append(dict(diametro_1))
    altura_2=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especies[2]]
    lista.append(dict(altura_2))
    diametro_2=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==especies[2]]
    lista.append(dict(diametro_2))
    return lista
#%%
#codigo mio
def leer_parque(nombre_archivo):
    f = open(nombre_archivo, encoding = 'utf8')## Le pasamos la ruta del archivo
    rows = csv.reader(f) ## Lee el archivo
    headers = next(rows) ## Identifica las columnas
    archivo = [] ## Creamos una lista vacía
    for row in rows: ## Iteramos en cada fila del archivo
        #print(row)
            
        d = {'Longitud': row[0], ## Creamos un diccionario con cada elemento
                 'Latitud': float(row[1]), ## del archivo que le pasamos
                 'id_arbol': str(row[2]),
                 'Altura_tot':float(row[3]),
                 'Diametro':float(row[4]),
                 'inclinacion': int(row[5]),
                 'Id_especie': int(row[6]),
                 'nombre_com': str(row[7]),
                 'nombre_cie': str(row[8]),
                 'tipo_folla': str(row[9]),
                 'espacio_ve': str(row[10]),
                 'ubicacion': str(row[11]),
                 'nombre_fam': str(row[12]),
                 'nombre_gen': str(row[13]),
                 'origen': str(row[14]),
                 'coord_x':(row[15]),
                 'coord_y': (row[16]),
                 
                }
        archivo.append(d)  
    return archivo        