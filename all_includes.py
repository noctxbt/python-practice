n = int(input())
first_digit = n % 10
total_sum = 0
count_number = str(n)
counter = len(count_number)
multiply = 1
average_nums = 0

while n != 0:
    last_digit = n % 10
    n = n // 10
    total_sum += last_digit
    multiply *= last_digit
    
    
    
average_nums = total_sum / counter
first_last = first_digit + last_digit

print(total_sum)
print(counter)
print(multiply)
print(average_nums)
print(last_digit)
print(first_last)
