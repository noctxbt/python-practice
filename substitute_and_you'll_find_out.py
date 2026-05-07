n, m = int(input()), int(input())

counter = 0

for banana in range(1, n):
    for diamond in range(1, n):
        for koza in range(1, n):
            if banana + 3 * diamond + 2 * koza == m:
                print( banana , ' + ', '3', '×', diamond , ' + ', '2', '×', koza, ' = ', m, sep='')
                counter += 1

if counter == 0:
    print('При заданных n и m решений не существует.')
