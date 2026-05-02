num = int(input())

check_num = num % 10
flag = True

while num != 0:
    last_digit = num % 10
    
    if last_digit != check_num:
        flag = False

    num //= 10

if flag:
    print('YES')
else:
    print('NO')
