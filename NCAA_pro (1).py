# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:15:27 2019

@author: ply
"""

#NCAA problem
from gurobipy import *
 
# create model
m = Model()
# Add decision variables 
# Let x1 : number of media people
# Let x2 : number of students from university
# Let x3 : number of general public
x1 = m.addVar(lb = 0,vtype = GRB.INTEGER, name = 'media')
x2 = m.addVar(lb = 0,vtype = GRB.INTEGER, name = 'university')
x3 = m.addVar(lb = 0,vtype = GRB.INTEGER, name = 'public')
m.update()
# set objective
obj = 45*x2 + 100*x3
m.setObjective(obj, GRB.MAXIMIZE)
# add constraints
con1 = m.addConstr(x1 + x2 + x3 <= 10000, name = 'total seat') 
# total seats are less than 10,000
con2 = m.addConstr(x2 - 0.5*x3 >= 0, name = 'seating constraint') 
#half the number of seats should go to competing univs
con3 = m.addConstr(x1 >= 500, name = 'reserved for media') 
#at least 500 seats for media
m.optimize()
#print solution and objective

for i in m.getVars():
    print(i.varName, i.x)
    
print('Objective:', m.objVal)