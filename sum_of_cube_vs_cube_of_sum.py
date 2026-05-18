a = int(input())
b = int(input())

sum_of_cube = a ** 3 + b ** 3
cube_of_sum = (a + b) ** 3

print(f'Для чисел {a} и {b}:')
print(f'  Сумма кубов: {a}**3 + {b}**3 = {sum_of_cube}')
print(f'  Куб суммы: ({a} + {b})**3 = {cube_of_sum}')