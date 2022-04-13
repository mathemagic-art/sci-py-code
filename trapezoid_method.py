# -*- coding: utf-8 -*-
"""Trapezoid_Method.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k1GV7Ivl7dzYKUz_ovvDAF92m2ve5zh4
"""

# Commented out IPython magic to ensure Python compatibility.
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sympy.abc import x
from sympy import *

func = input("Enter a Function: ")
f = sym.lambdify(x, func)
a = int(input("Enter starting point: "))
b = int(input("Enter ending point: "))
n = int(input("Number of intervals: "))
def Trapezoid(f,a,b):

  x = sym.symbols('x')

  f = sym.lambdify(x, func)

  dx = (b - a)/n

  A = 1/2 *(f(a) + f(b))
  for i in range(1, n):
      A = A + f(a + i*dx)
  Area = dx * A
  
  print("The area under the curve is", Area)

Trapezoid(f,a,b)

def Trapezoid_graph(f,a,b):
    X = np.linspace(a,b,100)
    x = np.linspace(a,b,n+1)
    Y = f(X)
    plt.figure(figsize = (15,10))
    plt.plot(X,Y, color='black', linewidth=2, markersize=50)

    for i in range(n):
        a = [x[i],x[i],x[i+1],x[i+1]]
        b = [0,f(x[i]),f(x[i+1]),0]
        plt.fill(a,b,'lightblue', edgecolor='black',alpha=1)

    plt.title('Area under the curve, Trapezoid method')
    # plt.show()
    plt.savefig('image.png')
Trapezoid_graph(f,a,b)