s = input()

while len(s) < 10:
    if len(s) % 4 == 0:
        s = s + 'x'
    elif len(s) % 5 == 0:
        s = s + 'y'
    else:
        s = 'z' + s

s = '@' + s

print(s)