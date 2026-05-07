n = int(input())

last_digit = n % 10
num3_count = 0
digit = last_digit
last_digit_count = 0
num_percent2_count = 0
sum_of_num = 0
multiply_of_num = 1
from_0_to_5 = 0

while n != 0:
    last_digit = n % 10
    if last_digit == digit:
        last_digit_count += 1
    if last_digit == 3:
        num3_count += 1
    elif last_digit % 2 == 0:
        num_percent2_count += 1
    if last_digit > 5:
        sum_of_num = last_digit + sum_of_num
    if last_digit > 7:
        multiply_of_num = last_digit * multiply_of_num
    if last_digit == 0 or last_digit == 5:
        from_0_to_5 += 1
    n //= 10

print(num3_count, last_digit_count, num_percent2_count, sum_of_num, multiply_of_num, from_0_to_5, sep='\n')
