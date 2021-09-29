# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:58:33 2021

@author: Alfredo
"""


## Ejercicio 5.3
import random
#import Counter
def cumpleanios():
    cumple=[]
    for i in range(30):
        cumple.append(random.randint(1,365))
    return cumple
## seleccionar días que más se repiten
def seleccionar_mejores(tirada):
    '''selecciona los dados que más se repiten 
    en una tirada dada.
    '''
    #cuento repeticiones
    T=Counter(tirada)

    #me fijo cual es el dado que más tengo
    d=T.most_common(1)[0][0] #día que más se repite
    n=T.most_common(1)[0][1] #cuantas veces se repite
    #esos los selecciono para la próxima mano
    seleccion =[d]*n

    return seleccion
def contar_mas_repetidos(seleccionar_mejores):
    mas_repetidos=len(seleccionar_mejores)
    print(f'La probabilidad de que cumplan más veces en un año es {mas_repetidos/30}%')
    return mas_repetidos
