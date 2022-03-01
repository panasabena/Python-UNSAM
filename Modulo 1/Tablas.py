# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 05:04:41 2022

@author: Alfredo
"""


## Calculadora de adelantos

#%%
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000.0
mes = 0
print('|','Mes','|','Total_pagado','|','Pago_mensual','|')
while mes < 61:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    print('|',mes,'|',saldo,'|',total_pagado)
while mes >=61 and mes <= 108:
    saldo = saldo * (1+tasa/12) - pago_mensual - adelanto # no entiendo por que aca es 1+tasa/12
    total_pagado = total_pagado + pago_mensual + adelanto
    mes = mes + 1
    print('|',mes,'|',saldo,'|',total_pagado)
while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual # no entiendo por que aca es 1+tasa/12
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    print('|',mes,'|',saldo,'|',total_pagado)
print ('Total pagado', round(total_pagado, 2))
print ('Cantidad de meses',mes)