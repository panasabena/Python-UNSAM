# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 03:54:11 2021

@author: Alfredo
"""


# Fosforos

lista_1 = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]

def propagar(lista):
    for i,f in enumerate(lista):
        if i -1 >=0:
            if f == 0 and lista[i-1]==1:
                lista[i] = 1
    for i in range(len(lista)-1,-1,-1):   
        if i + 1 < len(lista):
            if lista[i]==0 and lista[i+1] == 1:
                lista[i]= 1
                
    return lista