## geringoso.py
cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    if c != 'a' or 'e' or 'i' or 'o' or 'u':
        capadepenapa = capadepenapa + c
    if c == 'a':
        capadepenapa = capadepenapa + 'pa'
    if c == 'e':
        capadepenapa = capadepenapa + 'pe'
    if c == 'i':
        capadepenapa = capadepenapa + 'pi'
    if c == 'o':
        capadepenapa = capadepenapa + 'po'
    if c == 'u':
        capadepenapa = capadepenapa + 'pu'
print(capadepenapa) 
