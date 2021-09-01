# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

## Ejercicio 3.1
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i]=='A':
            
            return True
           
        else: ## Se saco el return False, porque nos estaba cortando el programa
            i += 1
            #print(i)

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%% Ejercicio 3.2 funciona abracadabra, devuelve solo un true
def tiene_a(expresion): ## No tenia los dos puntos
    n = len(expresion)
    i = 0
    while i<n: # No tenia los dos puntos
        ## Le agregue la condicion de ==A y los dos puntos
        ## Se corrigio el == a
        if expresion[i] == 'a' or expresion[i]=='A':
            return True
        i += 1
    return False ## Se cambio Falso por False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
## Funciona en las dos cadenas...

#%% Ejercicio 3.3
def tiene_uno(expresion):
    expresion=str(expresion)# se le cambia e tipo de dato a la variable expresion a str
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

















