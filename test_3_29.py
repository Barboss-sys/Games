import random

"""
Игра "Камень, Ножницы, бумага"
"""

def main():
    pc_chouse = random.randint(1, 3)
    player_chouse = get_inpun()
    result = pl_answer(player_chouse)
    pc_result = pc_answer(pc_chouse)

    print(f'В выбрали - {player_chouse}')
    if result == pc_chouse:
        print('Ничья')
        print(f'Компьюпер выбрал {pc_result}')
        main()
    elif result == 1 and pc_chouse == 3 or result == 3 and pc_chouse == 1:
        print('бумага заворачивает камень')
        print(f'Компьюпер выбрал {pc_result}')
    elif result == 2 and pc_chouse == 3 or result == 3 and pc_chouse == 2:
        print('ножницы режут бумагу')
        print(f'Компьюпер выбрал {pc_result}')
    elif result == 2 and pc_chouse == 1 or result == 1 and pc_chouse == 2:
        print('камень разбивает ножницы')
        print(f'Компьюпер выбрал {pc_result}')
    else:
        print('НЕДОПУСТИМЫЙ ВЫБОР !!!')


def get_inpun():
    p_c = input('Ваш Ход: ')
    return p_c

def pl_answer(arg):
    if arg == 'камень':
        result = 1
    elif arg == 'ножницы':
        result = 2
    elif arg == 'бумага':
        result = 3
    else:
        result = print('НЕДОПУСТИМОЕ ЗНАЧЕНИЕ !!!')
    return result

def pc_answer(arg):
    if arg == 1:
        result = 'камень'
    elif arg == 2:
        result = 'ножницы'
    elif arg == 3:
        result = 'бумага'
    else:
        result = print('НЕДОПУСТИМОЕ ЗНАЧЕНИЕ !!!')
    return result


if __name__ == '__main__':
    main()

