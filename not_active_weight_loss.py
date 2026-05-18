day = int(input())
mass = float(input())

n = 100 - 0.2 * day


if mass <= n:
    print('Все идет по плану')
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {mass} кг, ЦЕЛЬ по ВЕСУ = {n} кг')
else:
    print('Что-то пошло не так')
    print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {mass} кг, ЦЕЛЬ по ВЕСУ = {n} кг')




