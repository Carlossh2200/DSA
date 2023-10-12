# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:45:53 2023

@author: carlo
"""

archivo=open("LaNavidadEnLasMontanas.txt",mode='r',encoding='UTF-8')
archivoEscrito=open("ListaCompletaPalabras.txt",mode='w',encoding='UTF-8')
archivoEscritoOrdenado=open("ListaPalabrasOrdenadas.txt",mode='w',encoding='UTF-8')
diccionarioPrueba = []
diccionarioReal = []
numeroPalabras=0

def palabraNoRepetida(palabraNueva):
    contador=0
    for i in range(len(diccionarioPrueba)):
        if palabraNueva == diccionarioPrueba[i]:
            contador+=1
    if contador > 0:
        return 0
    elif contador==0:
        return 1

for fila in archivo:
    linea=fila.split()
    for i in range(len(linea)):
        palabraNueva=linea[i]
        if palabraNoRepetida(palabraNueva):    
            diccionarioPrueba.append(palabraNueva)
            archivoEscrito.write(palabraNueva)
            archivoEscrito.write('\n')
            numeroPalabras=numeroPalabras+1
            
def mergeSort(arreglo):
    longitud = int(len(arreglo))
    if longitud <= 1 : return
    
    puntoMedio = int(longitud / 2)
    tamanioArrDer = int(longitud-puntoMedio)
    arregloIzq= [0] * puntoMedio
    arregloDer = [0] * tamanioArrDer
    
    i = 0 #arreglo izq
    j = 0 #arreglo der
    
    for i in range(longitud):
        if i <  puntoMedio:
            arregloIzq[i]=arreglo[i]
        else:
            arregloDer[j]=arreglo[i]
            j+=1
    
    mergeSort(arregloIzq)
    mergeSort(arregloDer)
    merge(arregloIzq,arregloDer,arreglo)
            
    
    
    
def merge(arregloIzq, arregloDer, arreglo):
    tamanioIzq = len(arreglo) // 2
    tamanioDer = len(arreglo) - tamanioIzq
    i = 0
    izq = 0 
    der = 0
    
    while(izq < tamanioIzq and der < tamanioDer):
        if arregloIzq[izq] < arregloDer[der]:
            arreglo[i] = arregloIzq[izq]
            i+=1
            izq+=1
        else:
            arreglo[i]=arregloDer[der]
            i+=1
            der+=1
    
    while izq < tamanioIzq:
        arreglo[i]=arregloIzq[izq]
        i+=1
        izq+=1
    while der < tamanioDer:
        arreglo[i]=arregloDer[der]
        i+=1
        der+=1
    

print("Acomodando con mergeSort: \n")
mergeSort(diccionarioPrueba)
print("Escribiendo archivo con palabras ordenadas: ")
for palabra in diccionarioPrueba:
    archivoEscritoOrdenado.write(palabra)
    archivoEscritoOrdenado.write("\n")
print("Hecho")
print("numero de palabras : ",numeroPalabras)
archivoEscrito.write("Numero de palabras: ")
archivoEscrito.write(str(numeroPalabras))

    
