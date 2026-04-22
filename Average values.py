from math import sqrt

a = float(input())
b = float(input())

average_mean_numbers = (a + b) / 2
average_geometric_numbers = sqrt(a*b)
average_harmony_numbers = (2 * a * b) / (a + b)
average_square_numbers = sqrt((a ** 2 + b ** 2) / 2)

print(average_mean_numbers)
print(average_geometric_numbers)
print(average_harmony_numbers)
print(average_square_numbers)