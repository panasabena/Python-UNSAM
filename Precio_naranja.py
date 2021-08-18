## Data precios
data = open(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\precios.csv','rt')

for i in data:
    row=i.split(',')
    if row[0]=='Naranja':
        print('El precio de la naranja es: ',row[1])
