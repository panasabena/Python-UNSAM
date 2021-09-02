## hipoteca.py
saldo = 500000.0
tasa = 0.05
cuota = 2684.11
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes=0
suma_pagado=0
while mes <=(5*12):
    mes+=1
    saldo=saldo*(tasa/12 + 1)-cuota
    suma_pagado=suma_pagado+cuota
    print(mes,suma_pagado, saldo)
while mes >(5*12) and mes <=pago_extra_mes_fin and saldo>0:
    mes+=1
    saldo=saldo*(tasa/12 + 1)-cuota-pago_extra
    suma_pagado=suma_pagado+cuota+pago_extra
    print(mes,suma_pagado, saldo)
while mes >108 and saldo>=cuota:
    mes+=1
    saldo=saldo*(tasa/12 + 1)-cuota
    suma_pagado=suma_pagado+cuota
    print(mes,suma_pagado,saldo)
    if saldo<=cuota:
        mes+=1
        
        saldo_restante=saldo-saldo
        suma_pagado=suma_pagado+saldo
        print(mes,suma_pagado,saldo_restante)
print("Total pagado: ", suma_pagado)
print("Meses: ", mes)
print(f'pagó un total de {suma_pagado} hasta el mes {mes}')

