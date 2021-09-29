# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 23:48:39 2021

@author: Alfredo
"""


#Ejercicio 5.2 Generala

import random
tirada = []
for i in range(5):
    tirada.append(random.randint(1,6))
print(tirada)
#%%
def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada
def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
#%%
def tirar():
    tirada=[]
    es_generala=False
    pivot=0
    contador=0
    repetidos=[]
    pasadas=0
    while len(repetidos)<=6:
        tirada.append(random.randint(1,6))
        pasadas+=1
        for i in tirada:
            if tirada[contador]==pivot:
                repetidos.append(pivot)
            pivot=i    
        contador+=1
    if max(tirada)==min(tirada):
        es_generala=True

    return tirada, es_generala, repetidos

def es_generala(tirada):
    return max(tirada)==min(tirada)
#%%
    ## CODIGO DE RAFAEL GRIMSON
import numpy as np
from collections import Counter

def completar_tirada(seleccion):
    '''recibe los dados que se guardaron de una tirada anterior
    y completa tirando los que falta hasta 5'''
    tirada = seleccion
    while len(tirada)<5:
        tirada.append(np.random.randint(1,7))
    return tirada

def seleccionar_mejores(tirada):
    '''selecciona los dados que más se repiten 
    en una tirada dada.
    '''
    #cuento repeticiones
    T=Counter(tirada)

    #me fijo cual es el dado que más tengo
    d=T.most_common(1)[0][0] #dado que más se repite
    n=T.most_common(1)[0][1] #cuantas veces se repite
    
    #esos los selecciono para la próxima mano
    seleccion =[d]*n

    return seleccion

#%%​
N=100000   # vamos a jugar N manos de generala, cada una hasta 3 tiradas.
generalas=0 # cuento las generalas que saco​
for j in range(N):
    if j%10000==0:
        print(j)
    seleccion = [] #comienzo sin dados "seleccionados"
    for k in range(3):
        tirada = completar_tirada(seleccion) #completo tirando los dados que falten
        seleccion = seleccionar_mejores(tirada) # selecciono los repetidos
    #luego de las tres manos, si tengo 5 iguales, hice generala
    if len(seleccion) == 5:
        generalas += 1
print(f"Probabilidad de obtener generala haciendo mi mejor esfuerzo: {100*generalas/N}%")