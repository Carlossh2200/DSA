# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 07:22:33 2023

@author: carlo
"""
import networkx as nx

grafo=nx.Graph()
grafo.add_weighted_edges_from([('A','B',4),('A','C',2),('B','C',4),('C','D',3),('D','E',2)])

print("Los vertices del grafo son {}".format(list(grafo.nodes)))
print("Las aristas del grafo son {}".format(list(grafo.edges)))
print("El peso de la arista (A-B) es {}".format(grafo['A']['B']['weight']))
print("Las aristas del grafo y sus pesos son {}".format(list(grafo.edges(data=True))))