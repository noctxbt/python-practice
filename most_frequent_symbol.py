s = input()

a = 0
b = ''
for i in range(len(s)):
    if s.count(s[i]) >= a:
        a = s.count(s[i])
        b = s[i]

print(b)

        




