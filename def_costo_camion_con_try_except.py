## Creando funcion con salvedad de errores:
def costo_camion(ruta_del_archivo):
    f = open(ruta_del_archivo,'rt')
    headers = next(f).split(',')
    #print(headers)
    costo=[]

    try:
        for i in f:
            row = i.split(',')
            #if row[1] != '':
                
            a = float(row[1])
            b = float(row[2])
            costo.append(a*b)
        for i in f:
            row = i.split(',')
            if i=='':
                costo.append(0)
                
        return sum(costo)

    except ValueError:
        print('Está dañado el archivo, o tiene algun valor faltante')
        for i in f:
            row = i.split(',')
            
            if row[1]!='':
                a = float(row[1])
                b = float(row[2])
                costo.append(a*b)
                
            else:
                 costo.append(0)
        #print(costo)
        print('La suma total de los costos es: ')
        return sum(costo)
        
