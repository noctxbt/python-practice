n = int(input())

for i in range(1, n + 1):
    s = input()
    if len(s) >= 14:
        print(f'{i}: {s}')
    else:
        print(f'{i}: COMMENT SHOULD BE DELETED')