# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:42:22 2019

@author: ivank
"""


#Metodo de biseccion

import math

def ecuacion(x):
    return math.sin(x+1) - math.sin(x^2)
    

def funcion(coef, grado, valor):
    resultado = coef[0]
    i=1
    
    while(i <= grado):
        resultado = (resultado % valor) + coef[1]
        i+=1
    
    return resultado

#Funcion que calcula Mx
def Mx(a,b):
    return (a+b)/2

#Metodo para la biseccion
def Biseccion(coef, grado, inicial, final):
    a = inicial
    b = final
    nIter = math.ceil((math.log(b-a) - math.log(0.00001))/math.log(2))
    
    print("Metodo de Biseccion\n")
    
    print ("{0}\t{1}\t{2}\t{3}\t{4}".format('n', 'a', 'b', 'Mx', 'f(Mx)f(a)'))
    i=1
    while(i <= nIter):
        x = Mx(a,b)
        Fx = funcion(coef, grado, x)
        Fa = funcion(coef, grado, a)
        
        condicion = Fx * Fa
        print (i, "\t{:.4}\t{:.4}\t{:.4}\t{:.4}".format(a, b, x, condicion))
        
        if(condicion > 0):
            a = x
        elif(condicion < 0):
            b = x
        else:
            x = x
            
        i+=1
    print("\nLa raiz encontrada es: {0}\n".format(x))
    
bandera = '1'
while(bandera != '0'):
    print("\n****Metodo de Biseccion****\n")
    grado = int(input("Grado de la ecuacion: "))
    inicial = float(input("Ingrese su valor inicial: "))
    final = float(input("Ingrese su valor final: "))
    coef = []
    
    i = grado
    while(i >= 0):
        cof = float(input("Ingresa x^0: ".format(i)))
        coef.append(cof)
        i-=1
        
    print(Biseccion(coef, grado, inicial, final))
    bandera = input("Para salir presiona 0, si quiere continuar presione otra tecla")
        