n = int(input())

for i in range(1, n + 1):
    res = (((-1) ** (n + 1)) * (2 * n + 1) + 1) / 4
print(res)