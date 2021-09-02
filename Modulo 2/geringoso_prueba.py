#diccionario_geringoso.py
lista=['banana','manzana','mandarina']
capadepenapa_1 = ''
capadepenapa_2 = ''
capadepenapa_3 = ''
traduccion=[]
i=0
for c in lista[i]:
    if c != 'a' or 'e' or 'i' or 'o' or 'u':
        capadepenapa_1 = capadepenapa_1 + c
    if c == 'a':
        capadepenapa_1 = capadepenapa_1 + 'pa'
    if c == 'e':
        capadepenapa_1 = capadepenapa_1 + 'pe'
    if c == 'i':
        capadepenapa_1 = capadepenapa_1 + 'pi'
    if c == 'o':
        capadepenapa_1 = capadepenapa_1 + 'po'
    if c == 'u':
        capadepenapa_1 = capadepenapa_1 + 'pu'
traduccion.append(capadepenapa_1) 
i+=1
for c in lista[i]:
    #print(i)
    if c != 'a' or 'e' or 'i' or 'o' or 'u':
        capadepenapa_2 = capadepenapa_2 + c
    if c == 'a':
        capadepenapa_2 = capadepenapa_2 + 'pa'
    if c == 'e':
        capadepenapa_2 = capadepenapa_2 + 'pe'
    if c == 'i':
        capadepenapa_2 = capadepenapa_2 + 'pi'
    if c == 'o':
        capadepenapa_2 = capadepenapa_2 + 'po'
    if c == 'u':
        capadepenapa_2 = capadepenapa_2 + 'pu'
i+=1
traduccion.append(capadepenapa_2) 
for c in lista[i]:
    #print(i)
    if c != 'a' or 'e' or 'i' or 'o' or 'u':
        capadepenapa_3 = capadepenapa_3 + c
    if c == 'a':
        capadepenapa_3 = capadepenapa_3 + 'pa'
    if c == 'e':
        capadepenapa_3 = capadepenapa_3 + 'pe'
    if c == 'i':
        capadepenapa_3 = capadepenapa_3 + 'pi'
    if c == 'o':
        capadepenapa_3 = capadepenapa_3 + 'po'
    if c == 'u':
        capadepenapa_3 = capadepenapa_3 + 'pu'

traduccion.append(capadepenapa_3) 

print(traduccion)
print(i)
