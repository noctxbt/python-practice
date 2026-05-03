counter = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        counter = counter + 1

if counter > 0:
    print(counter)
    print(p)
else:
    print('NO')