##Listas como contenedores:
from pprint import pprint
import csv
...

def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        total=0.0
        for s in camion:
            total += s[1] * s[2]
        print(total)    
    return camion
    
## Lista de diccionarios:
def leer_camion(nombre_archivo): ## Le pasamos la ruta del archivo
    
    with open(nombre_archivo, 'rt') as f: ## Abre el archivo
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
        print (total) ## Imprimimos el total
        return camion ## Devuelve la lista 'camion'

## Segunda funcion:
def leer_precios(nombre_archivo):
    lista=[]
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        diccionario = {}
        for i,row in enumerate(rows):
            try:
                diccionario[row[0]] = float(row[1])
            except IndexError:
                print(f'Ups! no logro entender la linea {i+1}: {row}')
        return (diccionario)    

## Informe:
archivo_camion = (r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv')
archivo_precios = (r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\precios.csv')
camion = leer_camion(archivo_camion)
precios = leer_precios(archivo_precios)
costo_camion = 0
total_vendido = 0
for producto in camion:
    nombre = producto['Nombre']
    cajones = producto['Cajones']
    costo = producto['Precio']
    costo_camion +=  cajones * costo
    precio_venta = precios[nombre]
    total_vendido += cajones * precio_venta
balance = total_vendido - costo_camion
print('*'*22)
print('* Balance Verduleria *')
print('*'*22)
print(f'Costo camion: {costo_camion: .2f}\nVenta: {total_vendido: .2f}')
print(f'Balance: {balance: .2f}')
