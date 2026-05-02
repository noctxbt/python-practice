num = input()

counter = 0

for digit in num:
    if int(digit) % 2 == 0:
        counter += 1
        print(counter, '-я четная цифра равна ', digit, sep='')

if counter == 0:
    print('Четных цифр в числе нет')