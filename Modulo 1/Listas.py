# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 06:14:26 2022

@author: Alfredo
"""


## Listas


## Ejercicio 1.14

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])

#%%
cadena = 'Ejemplo con forc'
contador=0
for c in cadena:
    if 'c' in c:
        contador = contador +1
print('Cantidad de c:',contador)
#%%
## geringoso.py
cadena = input('Ingrese una palabra: ')
capadepenapa = ''
for c in cadena:
    if c != 'a' or 'e' or 'i' or 'o' or 'u':
        capadepenapa = capadepenapa + c
    if c == 'a':
        capadepenapa = capadepenapa + 'pa'
    if c == 'e':
        capadepenapa = capadepenapa + 'pe'
    if c == 'i':
        capadepenapa = capadepenapa + 'pi'
    if c == 'o':
        capadepenapa = capadepenapa + 'po'
    if c == 'u':
        capadepenapa = capadepenapa + 'pu'
print(capadepenapa)
print(cadena.lower())
#%%
lista_frutas = ['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Sandía', 'Pera']
print(lista_frutas[0])
print(lista_frutas[1])
print(lista_frutas[2])
print(lista_frutas[3])
#%%
print(lista_frutas[0:3])
print(lista_frutas[-2:])
compra = []
compra.append('Pera')
compra
lista_frutas[-2:] = compra
lista_frutas
#%%
# Ciclos sobre listas
for s in lista_frutas:
    print('s=', s)

#%%
# Usando operadores in, not in:
# Esta 'Granada' IN lista_frutas?
print('Granada' in lista_frutas)
# Esta 'Lima' IN lista_frutas? :
print('Lima' in lista_frutas)
# Esta 'Limon' NOT IN 'lista_frutas':
print ('Limon' not in lista_frutas)
#%%

## Adjuntar, insertar y borrar elementos:
# Agregar 'Mango'
print(lista_frutas)
lista_frutas.append('Mango')
print(lista_frutas)

## Usar el metodo insert para agregar Lima como segundo elemento de la lista
## Para usar este metodo, primero ponemos la lista, luego punto, luego
## la sentencia insert y dentro de insert (el indice, y el elemento)
## Como es muy probable que nos olvidemos:
# es importante que nos acordemos de help.



# help(lista_frutas.insert) ------> esto nos arroja el ayudin


lista_frutas.insert(2,'Lima')
print (lista_frutas)
#%%
lista_frutas = ['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
a = ','.join(lista_frutas)
a
b = ';'.join(lista_frutas)
b
c = ''.join(lista_frutas)
c





























