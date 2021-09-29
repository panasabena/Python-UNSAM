# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 23:47:24 2021

@author: Alfredo
"""


# Una forma de acercarce a pi
import matplotlib.pyplot as plt
import random
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
def estimar_pi():        
    N = 100000
    M = 0
    Xi = []
    Yi = []
    Xo = []
    Yo = []
    for i in range (N):
        x, y = generar_punto()
        if x**2 + y**2<1:
            Xi.append(x)
            Yi.append(y)
            M+=1
        else:
            Xo.append(x)
            Yo.append(y)
    plt.clf()
    plt.scatter(Xi,Yi, s=1)
    plt.scatter(Xo,Yo, s=1)  
    print(f'La proporcion que cae en\nel circulo es pi ~ {4*M/N:.5f}')
    