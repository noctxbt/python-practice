num = input()
cnt = 0
total = 1
while True:
    if len(str(num)) > 7:
        cnt += 1
    if int(num) % 100 == 11:
        break  
    total += 1
    num = input()

print(cnt, '/', total, sep='')