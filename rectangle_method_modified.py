# -*- coding: utf-8 -*-
"""Rectangle_Method_Modified.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lXF5JmlWmD8TCCBaWlmVnOhXY6m-ANC_
"""

# Commented out IPython magic to ensure Python compatibility.
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sympy.abc import x
from sympy import *
import math

def rectangle_Method(function:str, initial_point:int, end_point:int, num_of_interval:int)->str:
  x = sym.symbols('x')
  function = sym.lambdify(x, function)
  dx = (end_point - initial_point)/num_of_interval
  total = 0.0
  for i in range (num_of_interval):
          total = total + function((initial_point + (i*dx)))
  Area = dx*total
  return str(Area) 

rectangle_Method('e^x', 0, 2, 8)

# def rectangle_method_graph(function, initial_point, end_point, num_of_interval):
#     X = np.linspace(initial_point,end_point,100)
#     x = np.linspace(initial_point,end_point,num_of_interval+1)
#     z = sym.symbols('x')
#     function = sym.lambdify(z, function)
#     Y = function(X)
#     plt.figure(figsize = (15,10))
#     plt.plot(X,Y, color='black', linewidth=2, markersize=50)

#     for i in range(num_of_interval):
#         init_point = [x[i],x[i],x[i+1],x[i+1]]
#         end_point = [0,function(x[i]),function(x[i]),0]
#         plt.fill_between(init_point,end_point, edgecolor='black')
#         plt.savefig('Rectangle_Method_Graph.png')

# rectangle_method_graph("e^x", 0, 2, 8)