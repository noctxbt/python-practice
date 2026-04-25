n1 = int(input())

max1 = 0
max2 = 1

for i in range(1, n1 + 1):
    n2 = int(input())
    if n2 > max1:
        max2 = max1
        max1 = n2
    elif n2 > max2:
        max2 = n2
    
print(max1)
print(max2)
