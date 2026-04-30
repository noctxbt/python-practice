h1, m1 = int(input()), int(input())
h2, m2 = int(input()), int(input())

start = h1 * 60 + m1
end = h2 * 60 + m2

while start <= end:
    h = start // 60
    m = start % 60

    print(f'{h:02d}:{m:02d}')

    start += 1