num = int(input())
a = int((num / 100))
c = int((num % 100) / 10)
b = int(num % 10)


if max(a, b, c) - min(a, b, c) ==  (a + b + c) - (max(a, b, c) + min(a, b, c)):
    print('Число интересное')
else:
    print('Число неинтересное')

print(a, b, c)