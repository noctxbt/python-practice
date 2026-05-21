max_weight = -1
heaviest_word = ''

for _ in range(4):
    word = input()

    weight = 0

    for char in word:
        weight += ord(char)

    if weight > max_weight:
        max_weight = weight
        heaviest_word = word

print(heaviest_word)