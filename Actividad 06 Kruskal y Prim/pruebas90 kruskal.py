# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:01:04 2023

@author: carlo
"""

A_A = {
       "costo" : "0",
       "origen" : "A",
       "destino" : "A"
       }

A_B = {
     "costo" : "7",
     "origen" : "A",
     "destino" : "B"
     }

A_C = {
       "costo" : "8",
       "origen" : "A",
       "destino" : "C"
       }

B_D = {
       "costo" : "6",
       "origen" : "B",
       "destino" : "D"
       }

B_C = {
       "costo" : "3",
       "origen" : "B",
       "destino" : "C"
       }

B_F = {
       "costo" : "5",
       "origen" : "B",
       "destino" : "F"
       }

C_D = {
       "costo" : "4",
       "origen" : "C",
       "destino" : "D"
       }

C_F = {
       "costo" : "3",
       "origen" : "C",
       "destino" : "F"
       }

F_D = {
       "costo" : "2",
       "origen" : "F",
       "destino" : "D"
       }

F_E = {
       "costo" : "2",
       "origen" : "F",
       "destino" : "E"
       }

D_E = {
       "costo" : "5",
       "origen" : "D",
       "destino" : "E"
       }

E_E = {
       "costo" : "1",
       "origen" : "E",
       "destino" : "E"
       }



rutas = {
    "A_A" : A_A,
    "A_B" : A_B,
    "A_C" : A_C,
    "B_D" : B_D,
    "B_C" : B_C,
    "B_F" : B_F,
    "C_D" : C_D,
    "C_F" : C_F,
    "F_D" : F_D,
    "F_E" : F_E,
    "D_E" : D_E,
    "E_E" : E_E
    }


print("\n\n")

aristas=[A_A,A_B,A_C,B_D,B_C,B_F,C_D,C_F,F_D,F_E,D_E,E_E]

sorted_aristas = sorted(aristas, key=lambda x: int(x["costo"]))

nodosVisitados=[]

nodosFaltantes=['A','B','C','D','E','F']

costo = 0


for i in range(len(aristas)):
    if sorted_aristas[i]['destino'] not in nodosVisitados and not sorted_aristas[i]['origen']==sorted_aristas[i]['destino']:
        nodosVisitados.append(sorted_aristas[i]['destino'])
        print("Arista elegida: ",sorted_aristas[i])
        
        costo += int(sorted_aristas[i]['costo'])

print("costo total del árbol: ",costo)



    


