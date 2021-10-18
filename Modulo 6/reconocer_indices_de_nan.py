## Creo una lista vacia para guardar los indices(osea las filas) que no tienen ningun valor
## es decir que contienen "Nan"
lista=[]
for i, item in enumerate(data_recorridos['bici_estacion_destino']):
    
    try:
        int(item)
    except ValueError:
        lista.append(i)
        #print('ERROR at index {}: {!r}'.format(i, item))
lista
