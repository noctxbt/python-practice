n = int(input())
num = 0
total = 0
while n >= 10:
    temp = n
    total = 0
    
    while temp != 0:
        digit = temp % 10
        total += digit
        temp //= 10

    n = total
        


print(n)