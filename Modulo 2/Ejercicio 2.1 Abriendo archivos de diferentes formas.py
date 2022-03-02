# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## Ejercicio 2.1

f = open(r'C:\Users\fsabena\OneDrive - MicroStrategy, Inc\Programacion_en_Python_UNSAM-master\Programacion_en_Python_UNSAM-master\Notas\Ejercicios\ejercicios_python\Data\camion.csv')
with open(r'C:\Users\fsabena\OneDrive - MicroStrategy, Inc\Programacion_en_Python_UNSAM-master\Programacion_en_Python_UNSAM-master\Notas\Ejercicios\ejercicios_python\Data\camion.csv'):
    data = f.read()
f.close()
print(data)
#%%
## Leyendo el archivo en un ciclo for:
print('\nSegundo metodo:\n')
f = open(r'C:\Users\fsabena\OneDrive - MicroStrategy, Inc\Programacion_en_Python_UNSAM-master\Programacion_en_Python_UNSAM-master\Notas\Ejercicios\ejercicios_python\Data\camion.csv')

with open(r'C:\Users\fsabena\OneDrive - MicroStrategy, Inc\Programacion_en_Python_UNSAM-master\Programacion_en_Python_UNSAM-master\Notas\Ejercicios\ejercicios_python\Data\camion.csv'):
    for line in f:
        print (line, end = '')
#%%
## En ciertas ocasiones puede pasar que querramos leer una sola linea de
## texto (por ejemplo, queremos saltearnos la primera linea del archivo
## que contiene los nombres de las columnas)
f = open(r'C:\Users\fsabena\OneDrive - MicroStrategy, Inc\Programacion_en_Python_UNSAM-master\Programacion_en_Python_UNSAM-master\Notas\Ejercicios\ejercicios_python\Data\camion.csv')
headers = next(f)
print(headers)
for line in f:
    print(line, end = '')
#%%
# Me quede en 
# 'Una vez que estés leyendo un archivo línea a línea, podés hacer otras operaciones, como separar los datos dentro de una línea con el método split(). Por ejemplo, probá esto:'
f = open(r'C:\Users\fsabena\OneDrive - MicroStrategy, Inc\Programacion_en_Python_UNSAM-master\Programacion_en_Python_UNSAM-master\Notas\Ejercicios\ejercicios_python\Data\camion.csv')
headers = next(f).split(',')
print(headers)
for line in f:
    row = line.split(',')
    print(row)
f.close() ## Observar que tenemos que llamar a f.close() porque explicitamente
# no estamos trabajando con el comando with

## *Otra observación: usamos `../Data` para acceder a la carpeta "Data" 
## porque ésta se encuentra dentro de la carpeta "ejercicios_python", 
## al igual que la carpeta actual de trabajo, que es "Clase02". 
##Con los dos puntos del inicio del path nos referimos a la carpeta 
## "madre", es decir, a la carpeta que contiene a la actual.*


















