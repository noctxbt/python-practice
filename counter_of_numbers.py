word = input()

counter = 0

while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    word = input()
    counter += 1

print(counter)
    
