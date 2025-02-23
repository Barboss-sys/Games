

roll_pak = int(input('Введите число: '))

if roll_pak < 0 or roll_pak > 36:
    print('число вне диапазона !')

elif roll_pak == 0:
    print('Карман ЗЕЛЕНЫЙ')

elif roll_pak > 1 or roll_pak < 10:
    if roll_pak % 2 == 0:
        print('Карман ЧЕРНЫЙ')
    else:
        print('Карман КРАСТНЫЙ')

elif roll_pak > 11 or roll_pak < 18:
    if roll_pak % 2 == 0:
        print('Карман КРАСТНЫЙ')
    else:
        print('Карман ЧЕРНЫЙ')

elif roll_pak > 19 or roll_pak < 28:
    if roll_pak % 2 == 0:
        print('Карман ЧЕРНЫЙ')
    else:
        print('Карман КРАСТНЫЙ')

elif roll_pak > 29 or roll_pak < 36:
    if roll_pak % 2 == 0:
        print('Карман КРАСТНЫЙ')
    else:
        print('Карман ЧЕРНЫЙ')




