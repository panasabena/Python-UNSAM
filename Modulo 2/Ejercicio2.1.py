## Ejercicio 2.1, abriendo un archivo
with open (r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Github UNSAM\Programacion_en_Python_UNSAM-master\Notas\ejercicios_python\Data\camion.csv','rt') as f:
	data = f.read()
print(data)
