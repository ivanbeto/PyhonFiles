# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:34:15 2023

@author: ivank
"""

def fibonacci(posicion, debe_imprimirse):
    inicio = 0
    siguiente = 1
    for i in range(posicion+1):
        if(debe_imprimirse):
            print(str(inicio)+ ',', end="")
            tmp = inicio
            inicio = siguiente
            siguiente = siguiente + tmp
    return tmp
    


print(fibonacci(0,True))