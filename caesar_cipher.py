n = int(input())
s = input()

for i in range(len(s)):
    r = ord(s[i]) - n
    if r < 97:
        r = 122 - (96 - r)
    print(chr(r), end='')