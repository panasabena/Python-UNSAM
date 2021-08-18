try:
    s = input('Ingresá un numero entero: ')
    n = int(s)
    print(f' su inversa es {1/n:.3f}')
except ValueError:
    print('Error, no ingresaste un numero entero.')
except ZeroDivisionError:
    print('Error, no puedo dividir por cero.')
#%%
s = input ('Ingresa un numero entero: ')
if s.isnumeric():
    n = int(s)
    if n!=0:
        print(f'su inversa es {1/n:.3f}')
    else:
        print('Error, no puedo dividir por cero.')
else:
    print('Error, no ingresaste un numero entero')
        
