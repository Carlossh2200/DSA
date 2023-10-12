# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:07:36 2023

@author: carlo
"""

archivo=open("palabras.txt",mode='r',encoding='UTF-8')
archivoNuevo=open("archivoNuevo.txt",mode='w',encoding='UTF-8')
#palabras = archivo.readlines()
#print(palabras)
#frase = "El gato con botas"
#lista = frase.split()
#print(lista)
cuentaEspacios=0
contador=0
cuentaPalabras=0
for fila in archivo:
    contador=contador+1
    lista = fila.split()
    cuentaPalabras=cuentaPalabras+len(lista)
    cuentaEspacios+=len(lista)-1

archivoNuevo.write(str(contador))

       
print(cuentaEspacios)
print(contador)
print("Numero de palabras son: ",cuentaPalabras)
archivo.close()