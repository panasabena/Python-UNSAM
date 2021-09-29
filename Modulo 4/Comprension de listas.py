# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 23:21:49 2021

@author: Alfredo
"""


## Comprension de listas
a = [1,2,3,4,5]
b= []
for e in a:
    b.append(2*a)

b=[10*e for e in a]
print(b)

nombres = ['Daniel', 'Luz', 'Javier', 'Lissette']
nombre=[nombre.lower() for nombre in nombres]
nom = [nombre.upper() for nombre in nombres]

a = [1,-5,4,2,-2,10]
[2*x for x in a if x > 0]

# en matematica usamos {x^2| x pertenece a, x>0}
[x*x for x in a if x > 0]

# La sintaxis general es :
#[<expresion> for <variable> in <secuencia> if <condicion>]

l=[]
for x in a:
    if x>0:
        l.append(x)
    
#%%
lista = [0,1,2,3,4,5,6,7,8,9]

l2 = [x for x in range(10)]

# elementos pares
pares= [q for q in l2 if q%2==0]
