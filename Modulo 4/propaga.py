# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 04:06:20 2021

@author: Alfredo
"""


# Fosforos
# Pueden estar en tres estados:
# 1- Nuevos = 0
# 2- Prendidos fuego = 1
# 3- Ya gastados = -1
def propagar(fosforos):
    nuevo = 0
    encendido = 1
    carbonizado = -1
    pivot = 0
    estado=[]
    for i in fosforos:
        if i == nuevo:
            pivot = 0
            estado.append(pivot)
        elif i == encendido:
            pivot = 1
            estado.append(pivot)
        else:
            i = -1
            pivot = -1
            estado.append(pivot)
    return estado
fosforos = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
propagar(fosforos)
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
def propagar(fosforos):
    l= len(fosforos)-1
    for n, i in enumerate(fosforos):
        if i == 1 and n<l:
            if fosforos[n-1]==0:
                fosforos[n-1]=1
                if fosforos [n-2]==0:
                    z=n-1
                    for i in fosforos:
                        if fosforos[z] == 0 and z>0:
                            fosforos[z] = 1
                        z-=1
            if fosforos[n+1] == -1:
                fosforos[n+1]=-1
            if fosforos [n+1]==0:
                fosforos[n+1]=1
        return fosforos

fosforos = [0, 0, 0, 0, 0, 0,1, 0, 1, 0, 0]
propagar(fosforos)