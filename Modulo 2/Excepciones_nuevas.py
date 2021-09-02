## Puede pasar que si no especificamos el tipo de error, vamos a atrapar todas
## excepeciones.

numero_valido = False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
        print('No es valido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
