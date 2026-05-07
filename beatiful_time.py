n = int(input())

for i in range(0, 24):
    for j in range(0, 60):
        hour = i
        minute = j
        if hour ** n == minute:
            
            print(f'{hour:02d}:{minute:02d}')