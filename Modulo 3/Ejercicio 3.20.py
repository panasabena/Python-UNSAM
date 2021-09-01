from collections import Counter
def contar_ejemplares(lista_arboles):
    d = Counter()
    for arbol in lista_arboles:
        d[arbol['nombre_com']] += 1
    return d    
