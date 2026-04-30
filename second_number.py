num = int(input())

while num > 9:
    last_digit = num % 10
    num //= 10

print(last_digit)
    

