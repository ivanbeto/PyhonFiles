# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:08:01 2019

@author: ivanbeto
"""
import math

#Funcion que define la ecuacion a realizar
def funcion(x,y):
    return math.exp(-y)*(2*x-4)

#Metodo de Euler
def Euler(h, x0, y0):
    
    x=x0+h
    proceso = h*funcion(x0,y0)
    y = y0 + proceso
    
    return [x, y]

def main():
    print("=======Metodo de Euler=======\n")
    print("Indique el valor del paso h: ")
    h = float(input())
    print("Indique el valor inicial de x: ")
    x0 = float(input())
    print("Indique el valor inicial de y: ")
    y0 = float(input())
    
    iteracion=0

    for i in range(0,20):
        resultado = Euler(h,x0,y0)
        iteracion+=1
        print("=====================================")
        print("Iteracion: ",iteracion)
        print("\nx(",iteracion,") = ",resultado[0])
        print("y(",iteracion,") = ",resultado[1])
        print("=====================================")
        
        x0= resultado[0]    #El valor anterior se guarda para la siguiente iteracion
        y0= resultado[1]
    
    

#pi/2 es igual a 1.570796
#Para este caso la condicion inicial es y(0) = 1.570796
main()
