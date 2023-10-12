# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:13:59 2023

@author: carlo
"""

archivo=open("ListaPalabrasOrdenadas.txt",mode='r',encoding='UTF-8')

arreglo=[]

for fila in archivo:
    linea=fila.strip().split()
    arreglo.extend(linea)

def binarySearch(arreglo,objetivo):
    inicio = 0
    fin = len(arreglo)-1
    print("Palabra a buscar",objetivo)
   
    while inicio <= fin:
        
        medio = (inicio + (fin-1))//2
        pal=str(arreglo[medio])
        print(arreglo[medio])
    
        if (objetivo == pal):
            return medio - 1
        
        elif (objetivo < pal):
            fin = medio -1
        
        elif (objetivo != pal):
            print("La palabra no está en la lista, o la escribiste mal.")
            break
        
        else:
            inicio = medio +1
            
    return -1

objetivo=input("Que palabra quieres buscar?: ")
res=binarySearch(arreglo, objetivo)
if res != -1:
    print(f"La palabra '{objetivo}' se encontró en el indice '{res}'")
else:
    print("La palabra no se encontró...","\n")
        