# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 19:49:26 2023

@author: ivank
"""

#Programa para verificar numeros primos
def primos(num):
    for i in range(2, num):
        if(num % i) == 0:
            return False
    return True

print(primos(53))