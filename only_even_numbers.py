flag = 'YES'

for i in range(1, 11):
    n = int(input())
    if n % 2 != 0:
        flag = 'NO'

print(flag)