import random
import numpy as np
import matplotlib.pyplot as plt
    
# Le tenemos que pasar la cantidad de figuritas que tiene que tener el arreglo
def crear_album(figus_total): 
    return np.zeros(figus_total)
#%%
def album_incompleto(album):
    return 0 in album
#%%
def comprar_figu(figus_total):
    ''' recibe el número total de figuritas que tiene el álbum
    devuelve un número entero aleatorio que representa la figurita
    que nos tocó'''
    return random.randint(1,figus_total)-1
#%%
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    while album_incompleto(album):
        album[comprar_figu(figus_total)] +=1
    return album.sum()
cuantas_figus(6)
#%%
figus_total=6
n_repeticiones=1000
l=[]
for i in range(n_repeticiones):
    l.append(cuantas_figus(figus_total))
print(f'Para llenar el album de {figus_total} figus\ncompré en promedio {np.mean(l)} figus\n({n_repeticiones} repeticiones)')
#%%
figus_total=670
n_repeticiones=1000
figus_paquete=5
l=[]
for i in range(n_repeticiones):
    l.append(cuantas_figus(figus_total))
print(f'Para llenaar un album de {figus_total}\nfigus compré en promedio {np.mean(l)} figus\n({n_repeticiones} repeticiones)')
#%%
def comprar_paquete(figus_total, figus_paquete):
    '''en figus_total es la cantidad de figuritas que tiene el album
    y en figus_paquete es la cantidad de figuritas que trae por paquete'''
    p=[]
    for i in range(figus_paquete):
        p.append(comprar_figu(figus_total))
    return p
#%%
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
    return print('La cantidad de paquetes que tengo que comprar para llenar el album: ',album.sum()/figus_paquete)
#plt.hist(l,bins=50)

#%%
#Grafico de Tomas Bossi
def calcular_historia_figus_pegadas(figus_total,figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas
plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.show()
