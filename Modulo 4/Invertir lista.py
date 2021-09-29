# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 03:37:13 2021

@author: Alfredo
"""


def invertir_lista_v3(lista):
    invertida = []
    for e in lista:# Recorro la lista
        invertida = [e]+ invertida
    return invertida
lis_1=[1,2,3,4,5]
lis_2=['Bogotá', 'Rosario', 'Santiago', 'San Fernando',
       'San Miguel']
#%%

def invertir_lista_v2(lista):
    invertida= []
    for i in range(len(lista)-1,-1,-1):
        invertida.append(lista[i])
    return invertida
lis_2=['Bogotá', 'Rosario', 'Santiago', 'San Fernando',
       'San Miguel']
#%%
def invertir_lista(lista):
    invertida = []
    i = len(lista)-1
    while i >= 0:
        invertida.append(lista[i])
        i -= 1
    return invertida
