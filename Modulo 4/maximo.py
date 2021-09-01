# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 03:53:45 2021

@author: Alfredo
"""


#Ejercicio 4.4
def maximo(lista):
    pivot = lista[0] # iniciamos el elemento pivot con el cero
              # como elemento neutro
    for i in lista:
        if i > pivot:
            pivot = i
    return int(pivot)        
lista=[-99,-8,-5,-6,-5,-8,-7]
maximo(lista)