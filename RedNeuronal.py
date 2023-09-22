# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:41:16 2020

@author: ivank
"""
import csv
from Perceptron import Perceptron

class RedNeuronalArtificial:

    def __init__(self):
        self.tiposPan = []
        self.tiposRelleno = []
        self.entradas = []
        self.valoresDeseados = []
        
    def lecturaArchivo(self, nombreArchivo):
        
        with open(nombreArchivo) as archivo_csv:
            csv_lectura = csv.reader(archivo_csv, delimiter=',')
            lineaActual = 0
            
            for renglon in csv_lectura:
                #El primer renglon contiene el nombre de las columnas, por lo que se ignora
                if lineaActual == 0:
                    lineaActual +=1
                else:
                    x1 = self.addTipoPan(renglon[1])
                    x2 = self.addTipoRelleno(renglon[2])
                    x3 = self.addMantequilla(renglon[3])
                    
                    self.entradas.append([x1,x2,x3]) #Se asignan las entradas para el renglon actual
                    
                    #Se asigna un valor deseado de la funcion escalon para el renglon actual
                    if int(renglon[4]) >= 40:
                        self.valoresDeseados.append(1)
                    else:
                        self.valoresDeseados.append(0)
                    
                    lineaActual +=1
    
    #Funcion que asigna un valor numerico a los tipos de pan que se encuentran en la lista
    def addTipoPan(self, tipoPan):
        
        tamTiposPan = len(self.tiposPan)+1
        indiceTiposPan = len(self.tiposPan)
        
        if indiceTiposPan != 0:
            #Se busca si el tipo de pan ya esta en la lista de tipos de pan
            for i in range(0, indiceTiposPan):
                #Caso donde ya existe el tipo de pan en la lista
                if self.tiposPan[i][0] == tipoPan:
                    return self.tiposPan[i][1]
                
        #Caso donde no se encuenntra el tipo de pan en la lista        
        self.tiposPan.append([tipoPan,tamTiposPan])
        return tamTiposPan
        
    #Funcion que asigna un valor numerico a los tipos de relleno que se encuentran en la lista
    def addTipoRelleno(self, tipoRelleno):
        
        tamTiposRelleno = len(self.tiposRelleno)+1
        indiceTiposRelleno = len(self.tiposRelleno)
        
        if indiceTiposRelleno != 0:
            #Se busca si el tipo de relleno ya se encuentra en la lista
            for j in range(0, indiceTiposRelleno):
                #Caso donde ya se enceuentra el relleno en la lista
                if self.tiposRelleno[j][0] == tipoRelleno:
                    return self.tiposRelleno[j][1]
        
        #Caso donde no se encuentra el tipo de relleno y se agrega a la lista
        self.tiposRelleno.append([tipoRelleno,tamTiposRelleno])
        return tamTiposRelleno
        
    #Funcion que asigna un valor numerico dependiendo si se tiene o no mantequilla    
    def addMantequilla(self,tieneMantequilla):
        
        if tieneMantequilla == "yes":
            return 1
        elif tieneMantequilla == "no":
            return 0
        
    def printTiposPan(self):
        for i in range(len(rna.tiposPan)):
            print("Tipo de pan: ",rna.tiposPan[i][0]," ID: ",rna.tiposPan[i][1])
        
    def printTiposRelleno(self):
        for j in range(len(rna.tiposRelleno)):
            print("Tipo de Relleno: ",rna.tiposRelleno[j][0]," ID: ",rna.tiposRelleno[j][1])
    
    def printEntradas(self):
        for k in range(len(rna.entradas)):
            print("\nEntradas renglon", k+1, " ->  x1: ", rna.entradas[k][0],", x2: ", rna.entradas[k][1],", x3: ", rna.entradas[k][2],", Salida: ", rna.valoresDeseados[k])


#Int main(), programa principal
rna = RedNeuronalArtificial()
rna.lecturaArchivo('SandwichAnts.csv')

print("Programa proyecto 2 Inteligencia Artificial\n")
print("\n***Tabla de Tipos de Pan***\n")
rna.printTiposPan()

print("\n***Tabla de Tipos de Relleno***\n")
rna.printTiposRelleno()

print("\n***Tabla de entradas y de valores deseados x renglon***\n")
rna.printEntradas()

print("***\nEntrenamiento del perceptron simple***\n")
print("Los datos del entrenamiento, tanto dados como obtenidos, serán guardados en un archivo externo de extension csv")
perceptron = Perceptron(3,1,30)

print("\n\tPesos iniciales obtenidos de forma aleatoria")
for i in range(0, len(perceptron.pesos)):
    print("\t\tw",i," = ", perceptron.pesos[i])

TrainingTime = int(input("Ingrese un número de tiempo de entrenamiento del perceptron, las veces que estará entrenando: "))
perceptron.entrenamiento(rna.entradas[0:25], rna.valoresDeseados[0:25], TrainingTime, True)

print("\n****Pruebas del perceptron simple con las entradas iniciales****")
for i in range(len(rna.entradas)-8,len(rna.entradas)):
    print("\nEntradas actuales: ",rna.entradas[i])
    print("\nValores deseados (d): ",rna.valoresDeseados[i])
    
    resultado = perceptron.predecir(rna.entradas[i])
    print("\nValor obtenido (y): ",resultado)
    print("\nNumero de Error: ",rna.valoresDeseados[i] - resultado)
    
    if(resultado == 1):
        print("\nDebido al resultado, la conclusion es ----> El pan deberia tener 40 hormigas o más\n")
    elif(resultado == 0):
        print("\nDebido al resultado, la conclusion es ----> El pan deberia tener menos de 40 hormigas\n")
    print("***********************************************")