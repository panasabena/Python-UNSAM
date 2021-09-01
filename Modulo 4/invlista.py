# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 04:03:03 2021

@author: Alfredo
"""


#l = [1,2,3,4,5]
def invertir_lista(lista):
    '''Recibe una lista L y la devuelve invertida.'''
    invertida = []
    lista_nueva=lista.copy()
    i = len(lista_nueva)
    while i>0:
        i = i-1
        invertida.append(lista_nueva.pop(i))
    return invertida

    
#m = invertir_lista(l)
#print(f'Entrada{l}, Salida: {m}')