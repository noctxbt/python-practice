from math import *

n = int(input())

sumfactor = 0

for i in range(1, n + 1):
    sumfactor += factorial(i)

print(sumfactor)