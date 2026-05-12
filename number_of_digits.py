n = input()

counter = 0

for i in range(0, 10):
    counter += n.count(str(i))

print(counter)