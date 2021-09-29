# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 01:27:56 2021

@author: Alfredo
"""


import random
tirada = []
for i in range(5):
    tirada.append(random.randint(1,6))
print(tirada)

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada
def es_generala(tirada):
    return max(tirada)==min(tirada)
#%%
N = 1000000
salio_generala_servida = [es_generala(tirar()) for i in range (N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos aproximar la probabilidad de sacar generala servida mediante {prob}')
#%%
    # Python program to check if all 
# elements in a List are same 
res = False
  
def igual(lst):
    if len(lst) < 0 :
        res = True
    res = lst.count(lst[0]) == len(lst)
      
    if(res):
        print("Equal")
    else:
        print("Not equal")
# Driver Code
lst = ['Geeks', 'Geeks', 'Geeks', 'Geeks']
igual(lst)
#%%
N = 1000000
sumas = [sum(tirar()) for i in range(N)]
import matplotlib.pyplot as plt
## El density imprime la cantidad de resultados dividido la
## cantidad de experimentos
## En cambio cuando no le ponemos el density al histograma
## imprime la cantidad de veces que salió esa suma
## el bins es la cantidad de divisiones 
plt.hist(sumas, bins = 24)# , density = True) 
#%%
# Sin reposicion
from pprint import pprint        
palos = ['oro','copa', 'espada', 'basto']
valores = [1,2,3,4,5,6,7,8,9,10,11,12]
naipes = [(valor,palo) for valor in valores for palo in palos]
pprint(naipes)
#%%
## el sample lo que hace es tomar k numero aleatorio
# de elementos de la variable, sin reposicion.
random.sample(naipes, k = 40) 
print(naipes)
#%%
# por ejemplo en el truco se juega con 3 cartas, entonces
tres_cartas=random.sample(naipes, k = 3)
print(tres_cartas)
#%%
random.shuffle(naipes)
#%%
naipes = []
for i in valores:
    for j in palos:
        tupla = (j,i)
        naipes.append(tupla)
#%%
def generar_punto():
    x = random.random()
    y = random.random()
    return (x,y)
N = 100000
M = 0
for i in range (N):
    x,y = generar_punto()
    if x**2 + y**2 < 1:
        M+=1
print(f'pi ~ {4*M/N:.5f}')
#%%
import matplotlib.pyplot as plt
N=1000
M=0
Xi=[]
Yi=[]
Xo=[]
Yo=[]
for i in range(N):
    x,y = generar_punto()
    if x**2 + y**2 < 1:
        Xi.append(x)
        Yi.append(y)
        M+=1
    else:
        Xo.append(x)
        Yo.append(y)
print(f'pi ~ {4*M/N:.5f}')
#%%
plt.clf()
plt.scatter(Xi,Yi,s=1)
plt.scatter(Xo,Yo,s=1)
#%%

#random.randint() Devuelve un numero entre los dos parametros dados
#random.shuffle() Toma una secuencia y devuelve la secuencia mezclada
#random.choice() Toma un elemento
#random.choices() Toma n elementos con repeticion
#random.sample() Toma n elementos sin repeticion
#random.random() devuelve un random flotante entre 0 y 1
#random.gauss(mu,sigma) devuelve un random con distribucion gaussiana
#seed()         Fija un numero aleatorio















