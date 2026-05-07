s = input()

middle = (len(s) + 1) // 2

first_part = s[:middle]
second_part = s[middle:]

print(second_part + first_part)