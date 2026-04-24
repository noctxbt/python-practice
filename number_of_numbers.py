a = int(input())
b = int(input())

counter = 0

for _ in range(a, b + 1):
    if _ ** 3 % 10 == 4:
        counter = counter + 1
    elif _ ** 3 % 10 == 9:
        counter = counter + 1

print(counter)


