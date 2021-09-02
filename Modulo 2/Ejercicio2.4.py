# Ejercicio 2.4: Archivos comprimidos
import gzip ## Esta librería lee archivos comprimidos
with gzip.open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv.gz', 'rt') as f:
    for line in f:
        print(line,end = '')
    
