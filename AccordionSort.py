# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:54:59 2019

@author: ivank
"""
#Metodo del arcordeon
#Creado por Lisette Hernandez e Ivan Beto

def AccordeonSort(lista):
	#SI LA LISTA ESTA VACIA O ES DE UN ELEMENTO
    if(len(lista) <= 1):
        return list
    else:
        mitad =(len(lista)-1)/2
        final = len(lista)-1

        #PARA EL LADO IZQUIERO
        seguirI = 0 

        while(seguirI == 1):
            head = 0
            head2 = head +1
            seguirI = 1
			
            #PRIMER RECORRIDO
            for ii in range(0,mitad):
                if(lista[head] <= lista[head2]):
                    head = head + 1
                    head2 = head2 + 1
                    seguirI = seguirI +1

                else:
                    auxi = lista[head]
                    auxi2 = lista[head2]
                    lista[head] = auxi2
                    lista[head2] = auxi
                    head = head + 1
                    head2 = head2 + 1
                    seguirI = seguirI + 1
				
            #SEGUNDO RECORRIDO
            if(seguirI == 1) :
                seguirI = 1
                headreturn = mitad
                headreturn2 = headreturn -1
                for ji in range(0,mitad):
                    if(lista[headreturn] >= lista[headreturn2]):
                        headreturn = headreturn - 1
                        headreturn2 = headreturn - 1
                        seguirI = seguirI
					
                    else:
                        auxi3 = lista[headreturn]
                        auxi4 = lista[headreturn2]
                        lista[headreturn] = auxi4
                        lista[headreturn2] = auxi3
                        headreturn = headreturn - 1
                        headreturn2 = headreturn - 1
                        seguirI = seguirI + 1
			
			#PARA EL LADO DERECHO
            seguirD = 0
            while(seguirD == 1):
                tail = final
                tail2 = tail - 1
                seguirD = 1
				
				#PRIMER RECORRIDO
                for ider in range(mitad+1,final):
                    if(lista[tail] >= lista[tail2]):
                        tail = tail - 1
                        tail2 = tail2 - 1
                        seguirD = seguirD
                        
                    else:
                        auxd = lista[tail]
                        auxd2 = lista[tail2]
                        lista[tail] = auxd2
                        lista[tail2] = auxd
                        tail = tail - 1
                        tail2 = tail2 -1
                        seguirD = seguirD + 1
			
				#SEGUNDO RECORRIDO
                if(seguirD == 1):
                    seguirD = 1
                    tailreturn = mitad + 1
                    tailreturn2 = tailreturn + 1
                    for jder in range(mitad+1,final):
                        if(lista[tailreturn] <= lista[tailreturn2]):
                            tailreturn = tailreturn + 1
                            tailreturn2 = tailreturn + 1
                            seguirD = seguirD
					
                        else:
                            auxd3 = lista[tailreturn]
                            auxd4 = lista[tailreturn2]
                            lista[tailreturn] = auxd4
                            lista[tailreturn2] = auxd3
                            tailreturn = tailreturn + 1
                            tailreturn2 = tailreturn + 1
                            seguirD = seguirD + 1

				#PARA VERIFICAR QUE YA ESTE ORDENADA LA LISTA
                if(lista[mitad] <= lista[mitad+1]):
                    return lista

				#SI NO LO ESTA
                else:
                    inicio = 0
                    fin = mitad + 1
                    finTotal = (len(lista) - len(list)/2)
                    for x in range(inicio,finTotal):
                        if(lista[inicio] <= lista[fin]):
                            inicio = inicio + 1
                        else:
                            x = lista[fin]
                            lista.insert(inicio, x)
                            x = fin + 1
                            y = x + 1
                            lista[x:y] = []
                            inicio = inicio + 1
                            fin = fin + 1
    return lista
			
        
A= [2,13,12,45,16,76,54,89,60,92]
print(AccordeonSort(A))