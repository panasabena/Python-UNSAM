# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 02:27:26 2021

@author: Alfredo
"""

for i in range(0,10):
    print(f'{i:>7d}', end='')
print('\n--------------------------------------------------------------------------')
for i in range (0,10):
    for j in range(0,10):
        print(f'{i*j:<2d}', end='\t')
    print("")    