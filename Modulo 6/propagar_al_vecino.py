## Ejercicio 6.1
# Enunciado:
# El siguiente código propaga el fuego de cada fósforo encendido a sus vecinos
# inmediatos (si son fósforos nuevos) a lo largo de toda la lista. Y repite esta
# operación mientras sea necesario. ¿Te animás a estimar cuántas operaciones
# puede tener que hacer, en el peor caso?
def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e == 1 and i<n-1 and l[i+1] ==0:
            l[i+1] = 1
            modif = True
        if e == 1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m=l.copy()
    veces = 0
    while propagar_al_vecino(l):
        veces += 1
    print(f'Repeti {veces} veces la funcion propagar_al_vecino.')
    print(f'Con input {m}')
    print(f'Y obtuve {l}')
    return m
