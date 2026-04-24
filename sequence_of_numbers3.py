m, n = int(input()), int(input())

if m >= n:
    step = - 1
    stop = n - 1 
    start = m
if m <= n:
    step = 1
    stop = n + 1
    start = m
for i in range(start, stop, step):
    print(i)