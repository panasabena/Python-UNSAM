# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:12:24 2021

@author: Alfredo
"""


import random
tirada = []
for i in range(5):
    tirada.append(random.randint(1,6))
print(tirada)

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada
def es_generala(tirada):
    return max(tirada)==min(tirada)

#%%
N = 1000000
salio_generala_servida = [es_generala(tirar()) for i in range(N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
#%%


#%%
N = 10000
sumas = [sum(tirar()) for i in range(N)]
import matplotlib.pyplot as plt
plt.hist(sumas, bins = 24, density = True)
#%%
#sin reposicion
from pprint import pprint
palos= ['oro', 'copa', 'espada', 'basto']
valores = [1,2,3,4,5,6,7,10,11,12]
naipes = [(valor, palo) for valor in valores for palo in palos]
pprint(naipes)
# Random sample, te da los elementos que le pidas, sin reposicion
primera_mano=random.sample(naipes, k =3)
print(primera_mano)
# Random shuffle mezcla las cartas
primera_mano=random.shuffle(naipes)
#%%
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y
N = 100000
M = 0
for i in range(N):
    x,y = generar_punto()
    if x**2 + y**2 <1:
        M+=1
print(f'pi ~ {4*M/N:.5f}')
#%%

#%%
      
