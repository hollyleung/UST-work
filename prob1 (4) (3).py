# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:29:48 2019

@author: ply
"""

from gurobipy import *
import numpy as np

#set big M

M = 100000000

m = Model()

#define 9 decision variables x = [x1 x2 x3 x4], y=[y1 y2 y3 y4 y5]
x = m.addVars(4,lb = 0, vtype = GRB.INTEGER)
y = m.addVars(5,vtype = GRB.BINARY)

# set objective
c = np.array([70,60,90,80,-50000,-40000,-70000,-60000,0])

obj = LinExpr(c[0:4],x.select())+LinExpr(c[4:9],y.select())

m.setObjective(obj, GRB.MAXIMIZE)

#set constraints
A=np.array([[0,0,0,0,1,1,1,1,0],
   [0,0,0,0,-1,-1,1,0,0],
   [0,0,0,0,-1,-1,0,1,0],
   [5,3,6,4,0,0,0,0,-M],
   [4,6,3,5,0,0,0,0,M],
   [1,0,0,0,-M,0,0,0,0],
   [0,1,0,0,0,-M,0,0,0],
   [0,0,1,0,0,0,-M,0,0],
   [0,0,0,1,0,0,0,-M,0]
   ])

b = np.array([2,0,0,6000,6000+M,0,0,0,0])

m.addConstrs( LinExpr(A[i,0:4],x.select())+LinExpr(A[i,4:9],y.select()) <= b[i] for i in range(9))

m.optimize()

for i in m.getVars():
    print(i.varName,i.x)