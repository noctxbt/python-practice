s = input()
a = 0
b = 0
if s.count('h'):
    a = s.find('h')
    b = s.rfind('h') + 1
    print(s[:a], s[b:], sep='')