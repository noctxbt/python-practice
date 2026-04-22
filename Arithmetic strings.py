stroke = len(input())
stroke2 = len(input())
stroke3 = len(input())

progression = (2 * stroke2 - stroke3 - stroke) * (2 * stroke3 - stroke2 - stroke) * (2 * stroke - stroke2 - stroke3)

if progression == 0:
    print('YES')
else:
    print('NO')