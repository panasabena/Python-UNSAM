## Creamos una funcion que busca en el archivo
## la fruta y nos calcula el precio del cajón
def buscar_precio(fruta):
    data = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\precios.csv','rt')
    frutas=[]
    for i in data:
        fila = i.split(',')
        frutas.append(i[0])
        if fila[0] == fruta:
            precio = fila[1]
            print('El precio del cajon de ',fruta,'es: ', precio)
## Hasta acá funciona, el problema es cuando no encuentra la fruta...
    if fruta not in frutas:
        print(fruta,'no figura en el listado de precios.')
