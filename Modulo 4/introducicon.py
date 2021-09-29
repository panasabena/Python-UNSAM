# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 23:22:41 2021

@author: Alfredo
"""


def add (x,y):
    assert isinstance(x, int), 'Necesito un entero(int)'
    assert isinstance(x, int), 'Necesito un entero(int)'
    return x+y
#%%
    
def tiene_a(expresion):
    n = len(expresion)
    i = 0 
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1
        
rta = tiene_a('palabra')
print(rta)
#%%
def tabla():
    for x in range(5):
        for y in range(5):
            print(x*y)
#%%
def tabla():
    valor=0
    for x in range(5):
        for y in range(5):
            valor = valor+x
            print(valor)
tabla()
#%%
def tabla():
    
    for x in range(5):
        valor=0
        for y in range(5):
            print('x:',x,'y:',y,'val:',valor)
            print(valor)
            valor = valor+x
tabla()
#%%
def tabla(N):
    
    for x in range(N):
        valor=0
        for y in range(N):
            print('x:',x,'y:',y,'val:',valor)
            print(valor)
            valor = valor+x
tabla(N)