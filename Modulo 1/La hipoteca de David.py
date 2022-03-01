# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 03:39:17 2022

@author: Alfredo
"""


## La hipoteca de David
# David solicitó un crédito a 30 años para comprar una vivienda.
# Osea 30*12 = 360 meses
# Con una tasa nominal anual del 5%.
# Pidio $ 500000 al banco y acordo un pago mensual de $ 2684.11

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual # no entiendo por que aca es 1+tasa/12
    total_pagado = total_pagado + pago_mensual

print ('Total pagado', round(total_pagado, 2))
#%%
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000.0
mes = 0

while mes <=11:
    saldo = saldo * (1+tasa/12) - pago_mensual - adelanto # no entiendo por que aca es 1+tasa/12
    total_pagado = total_pagado + pago_mensual + adelanto
    mes = mes + 1
while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual # no entiendo por que aca es 1+tasa/12
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
print ('Total pagado', round(total_pagado, 2))
print ('Cantidad de meses',mes)















