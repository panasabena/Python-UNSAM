# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 02:43:09 2021

@author: Alfredo
"""


import random
import numpy as np
## Ejercicio 5.10
def crear_album(figus_total):
    figus_total=np.zeros(figus_total)
    return figus_total
## Ejercicio 5.11
def album_incompleto(figus_total):
    completo=True
    if 0 in figus_total:
        completo=True
    else:
        completo=False
    return completo
## Ejercicio 5.12
def comprar_figu(figus_total):
    n=len(figus_total)
    toco=(random.randint(1,n))
    return (f'Nos tocó la figurita {toco}')
## Ejercicio 5.13
def cuantas_figus(figus_total):
    n=len(figus_total) #tamaño del album
    album_nuevo=[]
    album_inicial=np.zeros(n)
    for i in range(n):
        album_nuevo.append(random.randint(1,n))
    try:
            
        for i in (album_nuevo):
            if i not in (album_inicial):
                album_inicial[i]=album_nuevo[i]
            else:
                pass
    except:
        print('Oh Oh, algo anduvo mal intente nuevamente')
    album_final=[]
    for item in album_inicial:
        if item not in album_final:
            album_final.append(item)
    arr=np.array(album_final)
    for i in arr:
        if i not in (album_inicial):
            album_inicial[i]=arr[i]
    return np.sort(arr)#,np.sort(album_inicial)
#%%
def cuantas_figus(figus_total):
    n=len(figus_total) #tamaño del album
    album_nuevo=[]
    album_inicial=[]
    for i in range(n):
        album_nuevo.append(random.randint(1,n))
    try:
        for i in (album_nuevo):
            if i not in (album_inicial):
                album_inicial.append(i)
            else:
                pass
    except:
        print('Oh Oh, algo anduvo mal intente nuevamente')
    #while len(album_inicial) < n:
    #    album_nuevo.append(random.randint(1,n))

    return len(sorted(album_inicial)),sorted(album_inicial)