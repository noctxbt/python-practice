a, b, c = int(input()), int(input()), int(input())

max = max(a, b, c)
min = min(a, b, c)
middle = (a + b + c) - min - max

print(max, middle, min, sep='\n')