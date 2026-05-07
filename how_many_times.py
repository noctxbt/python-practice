s = input()

counter_plus = 0
counter_star = 0

for i in range(0, len(s)):
    if s[i] == '+' :
        counter_plus += 1
    if s[i] == '*':
        counter_star += 1

print('Символ + встречается', counter_plus, 'раз')
print('Символ * встречается', counter_star, 'раз')