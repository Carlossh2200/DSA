# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:57:23 2023

@author: carlo
"""

A_B = {
     "costo" : "4",
     "origen" : "A",
     "destino" : "B"
     }

A_C = {
       "costo" : "2",
       "origen" : "A",
       "destino" : "C"
       }

B_C = {
     "costo" : "4",
     "origen" : "B",
     "destino" : "C"
     }

C_D = {
       "costo" : "3",
       "origen" : "C",
       "destino" : "D"
       }

C_E = {
       "costo" : "3",
       "origen" : "C",
       "destino" : "E"
       }

D_E = {
       "costo" : "2",
       "origen" : "D",
       "destino" : "E"
       }

rutas = {
    "A_B" : A_B,
    "A_C" : A_C,
    "B_C" : B_C,
    "C_D" : C_D,
    "C_E" : C_E,
    "D_E" : D_E,
    }

aristas=[A_B,A_C,B_C,C_D,C_E,D_E]

sorted_aristas = sorted(aristas, key=lambda x: int(x["costo"]))

nodosVisitados=[]

costo = 0

nodosFaltantes=['A','B','C','D','E']

for i in range(len(aristas)):
    if sorted_aristas[i]['destino'] not in nodosVisitados:
        nodosVisitados.append(sorted_aristas[i]['destino'])
        print("Arista elegida: ",sorted_aristas[i])
        costo += int(sorted_aristas[i]['costo'])

print("costo total del árbol: ",costo)