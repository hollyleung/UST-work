# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:52:44 2018

@author: ply
"""
import networkx as nx
#define a directed graph
G = nx.DiGraph() 
#add edges of the graph G 
#!!Attention!! Add source and terminal node manually
G.add_edges_from([(1, 2, {'capacity': 200}),
                   (1, 3, {'capacity': 300}),
                   (2, 4, {'capacity': 125, 'weight': 425}),
                   (2, 5, {'capacity': 150, 'weight': 560}),
                   (3, 4, {'capacity': 175, 'weight': 510}),
                   (3, 5, {'capacity': 200, 'weight': 600}),
                   (4, 6, {'capacity': 100, 'weight': 470}),
                   (4, 7, {'capacity': 150, 'weight': 505}),
                   (4, 8, {'capacity': 100, 'weight': 490}),
                   (5, 6, {'capacity': 125, 'weight': 390}),
                   (5, 7, {'capacity': 150, 'weight': 410}),
                   (5, 8, {'capacity': 75, 'weight': 440}),
                   (6, 9, {'capacity': 150, 'weight': 0}),
                   (7, 9, {'capacity': 200, 'weight': 0}),
                   (8, 9, {'capacity': 150, 'weight': 0})])
#solve the problem
mincostFlow = nx.max_flow_min_cost(G, 1, 9)
mincost = nx.cost_of_flow(G, mincostFlow)
print(mincost)
print(mincostFlow)
#===================================================================
import networkx as nx
#define a directed graph
G = nx.DiGraph() 
#add edges of the graph G 
#!!Attention!! Add source and terminal node manually
G.add_edges_from([(1, 2, {'capacity': 200}),
                   (1, 3, {'capacity': 300}),
                   (2, 4, {'capacity': 125, 'weight': 425}),
                   (2, 5, {'capacity': 150, 'weight': 560}),
                   (3, 4, {'capacity': 175, 'weight': 510}),
                   (3, 5, {'capacity': 200, 'weight': 600}),
                   (4, 6, {'capacity': 100, 'weight': 470}),
                   (4, 7, {'capacity': 150, 'weight': 505}),
                   (4, 8, {'capacity': 100, 'weight': 490}),
                   (5, 6, {'capacity': 125, 'weight': 390}),
                   (5, 7, {'capacity': 150, 'weight': 410}),
                   (5, 8, {'capacity': 75, 'weight': 440}),
                   (6, 9, {'capacity': 150}),
                   (7, 9, {'capacity': 200}),
                   (8, 9, {'capacity': 150})])
#solve the problem
mincostFlow = nx.max_flow_min_cost(G, 1, 9)
mincost = nx.cost_of_flow(G, mincostFlow)
print(mincost)
print(mincostFlow)