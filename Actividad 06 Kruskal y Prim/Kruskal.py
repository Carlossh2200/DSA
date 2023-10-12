# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:01:04 2023

@author: carlo
"""

A_B = {
     "costo" : "2",
     "origen" : "A",
     "destino" : "B"
     }

A_D = {
       "costo" : "1",
       "origen" : "A",
       "destino" : "D"
       }

A_E = {
     "costo" : "4 ",
     "origen" : "A",
     "destino" : "E"
     }

B_D = {
       "costo" : "3",
       "origen" : "B",
       "destino" : "D"
       }

B_C = {
       "costo" : "3",
       "origen" : "B",
       "destino" : "C"
       }

B_F = {
       "costo" : "7",
       "origen" : "B",
       "destino" : "F"
       }

F_C = {
       "costo" : "8",
       "origen" : "F",
       "destino" : "C"
       }

C_D = {
       "costo" : "5",
       "origen" : "C",
       "destino" : "D"
       }

D_E = {
       "costo" : "9",
       "origen" : "D",
       "destino" : "E"
       }


rutas = {
    "A_B" : A_B,
    "A_D" : A_D,
    "A_E" : A_E,
    "B_D" : B_D,
    "B_C" : B_C,
    "B_F" : B_F,
    "F_C" : F_C,
    "C_D" : C_D,
    "D_E" : D_E,
    }


print("\n\n")

aristas=[A_B,A_D,A_E,B_D,B_C,B_F,F_C,C_D,D_E]

sorted_aristas = sorted(aristas, key=lambda x: int(x["costo"]))

nodosVisitados=[]

nodosFaltantes=['A','B','C','D','E','F']

costo = 0

for i in range(len(aristas)):
    if sorted_aristas[i]['destino'] not in nodosVisitados:
        nodosVisitados.append(sorted_aristas[i]['destino'])
        print("Arista elegida: ",sorted_aristas[i])
        costo += int(sorted_aristas[i]['costo'])

print("costo total del árbol: ",costo)




    


