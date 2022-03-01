# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 05:56:23 2022

@author: Alfredo
"""


## Cadenas
s = 'Buenos dias'
n = 'Francisco Alfredo'
print (s,n)
#%%
## Ubicando pedazos de la cadena
print(s[0])
print(s[1])
print(s[0:5])

## Primeras operaciones

# La siguiente linea de comando devuelve un True o un False, si se encuentra
# la letra 'a' en la variable s
print('a' in s)
print('A' in s)

## Descubriendo errores o interpretando el error

# Nos devuelve un error que dice 'String index out of range', lo que significa
# que el indice de la cadena, esta fuera de rango, entonces para poder ver
# cuantos caracteres o elementos tiene nuestra cadena, podemos usar el len()
print (len(s)) 
print (s[11])
