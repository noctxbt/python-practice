s = input()
for i in range(0, len(s)):
    if s[i] in '1234567890':
        print('Цифра')
        break
else:
    print('Цифр нет')
        