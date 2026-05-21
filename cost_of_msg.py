s = input()
price = 0
for i in range(len(s)):
    price += ord(s[i])
    

summ = price * 3
print(summ)

print(f"Текст сообщения: '{s}'")
print(f"Стоимость сообщения: {summ}🐝")
