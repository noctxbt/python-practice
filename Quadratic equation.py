from math import sqrt

a = float(input())
b = float(input())
c = float(input())

a != 0

D = (b ** 2) - (4 * a * c)

if D < 0:
    print('Нет корней')
elif D == 0: 
    print(-b / (2 * a))
elif D > 0:
    x1 = ((-b + sqrt(D)) / (2 * a))
    x2 = ((-b - sqrt(D)) / (2 * a))
    if x1 > x2:
        print(x2)
        print(x1)
    elif x2 > x1:
        print(x1)
        print(x2)
    