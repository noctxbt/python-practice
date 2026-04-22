from math import tan, pi

n = int(input())
a = float(input())

res = (n * a ** 2) / (4 * tan(pi/n))

print(res)