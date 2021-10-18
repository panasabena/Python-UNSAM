## Busco indices de valores nulos:
esnulo=[]
for i, item in enumerate(data['dirección_completa'].isnull()):
    if item==True:
        esnulo.append(i)
print(f'Hay {len(esnulo)} valores nulos y son en los indices:\n{esnulo}')
