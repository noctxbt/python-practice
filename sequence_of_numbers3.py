m, n = int(input()), int(input())

if m % 2 == 1:
    start = m
else:
    start = m - 1

end = n - 1

for i in range(start, end, -2):
    print(i)