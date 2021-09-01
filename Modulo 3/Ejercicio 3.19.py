def especies (lista_arboles):
    lista=[]
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    return set(lista)    
