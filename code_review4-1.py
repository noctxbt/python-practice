n = int(input())
max_digit = n % 10

while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n //= 10

if max_digit == 5:
    print('NO')
elif max_digit == 7:
    print('0')
else:
    print(max_digit)