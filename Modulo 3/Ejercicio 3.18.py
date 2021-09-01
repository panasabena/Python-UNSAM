# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:08:40 2021

@author: Alfredo
"""
from collections import Counter
#%%
import csv
ruta_del_archivo = (r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\arbolado-en-espacios-verdes.csv')
def leer_archivo(ruta_del_archivo):
    f = open(ruta_del_archivo, encoding = 'utf8')## Le pasamos la ruta del archivo
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
#%%
nombre_archivo = (r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\arbolado-en-espacios-verdes.csv')
parque='GENERAL PAZ'
def leer_parque(nombre_archivo,parque):
    lista=[]
    with open (nombre_archivo, encoding= 'utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            registro=dict(zip(encabezados, fila))
            if registro['espacio_ve']==parque:
                lista.append(registro)
    return lista
nombre_archivo = leer_parque(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

#%%
#3.19
def especies (lista_arboles):
    lista=[]
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    return set(lista)
#%%
# 3.20
def contar_ejemplares(lista_arboles):
    d = Counter()
    for arbol in lista_arboles:
        d[arbol['nombre_com']] += 1
    return d

#%% 3.21
def leer_parque(nombre_archivo, parque):
    lista = []
    with open (nombre_archivo, encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            registro = dict(zip(encabezados, fila))
            registro['altura_tot'] = float(registro['altura_tot'])
            if registro['espacio_ve'] == parque:
                lista.append(registro)
        return lista
gral_paz = leer_parque(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

def obtener_alturas(lista_arboles, especie):
    lista = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista.append(arbol['altura_tot'])
    return lista


alturas_jac_gral_paz=obtener_alturas(gral_paz,'Jacarandá')
#%%
def obtener_inclinaciones(lista_arboles,especie):
    lista=[]
    for arbol in lista_arboles:
        if arbol['nombre_com']== especie:
            lista.append(arbol['inclinacio'])
    return lista
inclinaciones=obtener_inclinaciones(gral_paz,'Jacarandá')
