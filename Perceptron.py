# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:44:14 2020

@author: ivank
"""
import numpy as np
import random
import csv

class Perceptron:
	
    #Constructor de la clase perceptron
    def __init__(self, numEntradas, factorAprend, valorActivacion):
        self.pesos = np.zeros(numEntradas+1)  #Pesos de la capa de la red + valor de umbral
        self.factorAprend = factorAprend        #Valor del factor de aprendizaje
        
        for i in range(0,len(self.pesos)):
            self.pesos[i] = round(random.uniform(0,1),4)
    
    #Funcion de predicciones
    def predecir(self, entradas):
        #Donde se realiza la sumatoria de los valores
        sumatoriaTotal = np.dot(entradas, self.pesos[1:]) + self.pesos[0]
        
        #Funcion escalon
        if sumatoriaTotal >= 40:
            funcion = 1
        else:
            funcion = 0
        
        return funcion
    
    #Funcion donde se entrena al perceptron durante un tiempo determinado
    def entrenamiento(self, entradas, valorDeseado, tiempoTraining, umbralVar):
        
        #Se almacena la informacion obtenida del entrenamiento en un archivo extreno, para un analisis posterior
        with open('Entrenamiento.csv', mode='w') as archivoEntrenamiento:
            csv_write = csv.writer(archivoEntrenamiento, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_write.writerow(['Iteracion','x1','x2','x3','d','w1','w2','w3','w0','y','error'])
            
            cont = 1
            while cont <= tiempoTraining:
                for x, d in zip(entradas, valorDeseado):
                    y = self.predecir(x)
                    error = d-y   #Resta entre la funcion y el valor obtenido, margen de error
                    
                    #Momento de escritura de los datos obtenidos en ese momento
                    csv_write.writerow([cont,x[0],x[1],x[2],d,self.pesos[1],self.pesos[2],self.pesos[3],self.pesos[0],y,error])
                    
                    #Modificacion de los pesos
                    for i in range(0, len(x)):
                        self.pesos[i+1] += self.factorAprend + error + x[i]
                        
                    if umbralVar == True:
                        self.pesos[0] = self.factorAprend + error
                        
                cont +=1
                    
                    
                    
                    