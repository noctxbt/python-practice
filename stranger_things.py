msg = int(input())

counter = 0

for i in range(1, msg + 1):
    n = input()
    if n.count('11') >= 3:
        counter += 1

print(counter)