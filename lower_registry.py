s1 = input()
s2 = s1.upper()

counter = 0

for i in range(0, len(s2)):
    if s1[i] != s2[i] and s1[i] in 'abcdefghijklmnopqrstuvwxyz':
        counter += 1

print(counter)