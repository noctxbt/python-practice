from math import log

n = int(input())

num = 0
num2 = 0

for i in range(1, n):
    num = num + (1 / (i + 1))
    
num2 = num + 1 - log(n)

print(num2)