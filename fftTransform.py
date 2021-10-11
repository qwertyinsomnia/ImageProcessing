import math as mt
import cmath as cm
import numpy as np

A=[[1, 0.25, 0.25], [0.25, -0.5, -0.5], [0.25, -0.5, -0.5]]

m=len(A)
n=len(A[0])
B=[[0 for i in range(m)] for j in range(n)]
t=1.0/m/n


for u in range(m):
    for v in range(n):
        sum=0
        for x in range(m):
            for y in range(n):
               sum=sum+A[x][y]*cm.exp(-2j*mt.pi*(u*x/float(m)+v*y/float(n)))
               #print sum
        #print sum.real
        if abs(sum.real)<10**-6:            
            B[u][v]=0
        else:
            B[u][v]=t*(sum.real)


for i in range(m):
    for j in range(n):
        print (B[i][j], end=" ")
    print()
   