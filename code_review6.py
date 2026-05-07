n = int(input())
s = 0
total = 0
while n != 0:
    if n % 2 == 0:
        s = n % 10
        total += s
    n //= 10
print(total)