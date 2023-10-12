# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:46:49 2023

@author: carlo
"""

def binarySearch(arreglo, objetivo):
    inicio = 0
    fin = len(arreglo) - 1
    print("Palabra a buscar:", objetivo)
    
    while inicio <= fin:
        medio = inicio + (fin - inicio) // 2
        valor = str(arreglo[medio])
        
        print("medio:", valor)
        
        if valor < objetivo:
            inicio = medio + 1
        elif valor > objetivo:
            fin = medio - 1
        else:
            return medio
    
    return -1

# Example usage:
words = ["aquella","(pues","(y","--Ahí"]
target = "(y"
result = binarySearch(words, target)
print("Result:", result)





