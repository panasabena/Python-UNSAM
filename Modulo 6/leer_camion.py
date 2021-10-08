# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:22:48 2021

@author: Alfredo
"""


# Scripts
# Definir Nombres
def cuadrado(x):
   
    return (f'El cuadrado de {x} es {x*x}')
#%%
def leer_precios(nombre_archivo):
    '''Los precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre: precio, ...}
    '''
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[0])
    return precios
#%%
def costo_camion(nombre_archivo):
    '''Devuelve una lista de diccionarios, cada diccionario, es un renglon del archivo.
    '''
    camion=[]
    f = open(nombre_archivo, 'rt')
    filas = csv.reader(f)
    encabezados = next(filas)
    costo_total=0
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        camion.append(record)
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
            
            if fila != '':
                print(record)
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar {fila}')
    return camion
#%%
# tabla_informe.py
import csv

def leer_camion(nombre_archivo):
    '''
    Lee un archivo de lotes en un camión 
    y lo devuelve como lista de diccionarios con claves
    nombre, cajones, precio.

    '''
    camion = []
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            cajon = {
                'nombre' : record['nombre'],
                'cajones' : int(record['cajones']),
                'precio' : float(record['precio'])
            }
            camion.append(cajon)
    return camion