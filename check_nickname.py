nick = input()
nick_len = len(nick)

if 5 <= nick_len <= 15 and nick.startswith('@') and nick[1:].isalnum() and nick[1:] == nick[1:].lower():
    print('Correct')
else:
    print('Incorrect')