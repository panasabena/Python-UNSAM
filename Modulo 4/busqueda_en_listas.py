# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 02:34:42 2021

@author: Alfredo
"""


def busqueda_con_index(lista,e):
    '''Busca un elemento e en la lista.
    Si e está en la lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1
    return pos
#%%
def busqueda_lineal(lista,e):
    ''' Si e está en la lista devuelve su posición
    de lo contrario devuelve -1
    '''
    pos = -1
    i = 0
    for z in lista:
        if z == e:
            pos = i 
            break
        i+=1
    return pos
#%%
#Version con enumerate
def busqueda_enumerate(lista,e):
    ''' Si e está en la lista devuelve su posición
    de lo contrario devuelve -1
    '''
    pos = -1 # comenzamos suponiendo que no está
    for i, z in enumerate(lista): #recorremos la lista
        if z==e:    # si encontramos a e
            pos = i # guardamos su posición
            break   # y salimos del ciclo
    return pos
#%%
def buscar_u_elemento(lista,e):
    ''' Si e está en la lista devuelve su posición
    de lo contrario devuelve -1
    '''
    pos = -1 # comenzamos suponiendo que no está
    apa = 0
    for i, z in enumerate(lista): #recorremos la lista
        if z==e:    # si encontramos a e
            apa +=1
            pos = i # guardamos su posición
            #break   # y salimos del ciclo
    if apa>0:
        return (f'Aparece {apa} veces')
    else:
        return pos
lista=buscar_u_elemento([5,8,4,5,8,6,2,1,0,7],5)

#%%
def maximo(lista):
    pivot = lista[0] # iniciamos el elemento pivot con el cero
              # como elemento neutro
    for i in lista:
        if i > pivot:
            pivot = i
    return pivot        
lista=[-99,-8,-5,-6,-5,-8,-7]
maximo(lista)
#%%
def minimo(lista):
    pivot=lista[0]
    for i in lista:
        if i < pivot:
            pivot = i
    return pivot

        
    
    
    
    
    