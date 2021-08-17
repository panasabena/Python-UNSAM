#inclusive.py
frase=input('Ingrese su texto sin traducir: ')
frase=frase.split(' ')
#print (frase)
lista=[]
traducida=[]
for i in frase:
    lista.append(list(i))
for i in lista:
    if len(i)<2:
        lista=''.join(i)
        traducida.append(lista)
        pass
    elif i[-2]=='o':
        i[-2]='e'
        lista=''.join(i)
        traducida.append(lista)
    elif i[-2]=='ó':
        i[-2]='é'
        lista=''.join(i)
        traducida.append(lista)
    else:
        lista=''.join(i)
        traducida.append(lista)
traducida=' '.join(traducida)
print(traducida)
