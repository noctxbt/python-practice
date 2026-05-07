s = input()

counter1 = 0
counter2 = 0

for i in range(0, len(s)):
    if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        counter1 += 1
    if s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        counter2 += 1

print('Количество гласных букв равно', counter1)
print('Количество согласных букв равно', counter2)
    
