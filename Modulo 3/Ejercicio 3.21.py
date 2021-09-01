import csv
def leer_parque(nombre_archivo, parque):
    lista = []
    with open (nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            registro = dict(zip(encabezados, fila))
            registro['altura_tot'] = float(registro['altura_tot'])
            if registro['espacio_ve'] == parque:
                lista.append(registro)
        return lista
gral_paz = leer_parque(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')    


def obtener_alturas(lista_arboles, especie):
    lista = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista.append(arbol['altura_tot'])
    return lista       
