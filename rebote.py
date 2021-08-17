## rebote.py
pique=0
altura=100
piso=3/5
rebote=100
while pique < 10:
    pique+=1
    rebote-=rebote-(rebote*piso)
    print(round(rebote,4))
