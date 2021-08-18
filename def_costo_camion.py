## Ejercicio 2.6: Transformar un script en una función
def costo_camion(ruta_del_archivo):
    f = open(ruta_del_archivo,'rt')
    headers = next(f).split(',')
    #print(headers)
    costo=[]
    for i in f:
        row = i.split(',')
        a = float(row[1])
        b = float(row[2])
        costo.append(a*b)
    return sum(costo)
