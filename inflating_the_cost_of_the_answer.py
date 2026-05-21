s = input()

chrcount = 0
chrcounttr = 0

eng = 'eyopaxcETOPAHXCBM'
ru = 'еуорахсЕТОРАНХСВМ'

trans = str.maketrans(eng, ru)

for i in range(len(s)):
    chrcount += ord(s[i])
    chrcounttr += ord(s.translate(trans)[i])

print(f'Старая стоимость: {chrcount * 3}🐝') 
print(f'Новая стоимость: {chrcounttr * 3}🐝') 