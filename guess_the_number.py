

def find_number(my_number):
    print('Угадай чило котороя я забдумал !')
    print('я загадал число от 1 до 100')
    print('у тебя 10 попыток')
    print('Удачи!')
    my_number = range(101)
    my_n = str(my_number)
    find_n = input('Введите ваше число: ')
    while True:
        if find_n == 'нет':
            print('Пока!')
            break
        elif find_n < my_n:
            print('Не верно мое число больше!')
        elif find_n > my_n:
            print('Не верно мое число меньше!')
        else:
            print('Верно ! , съиграем еще раз? (да /нет)')
            if find_n == 'да':
                find_number(range(101))



find_number(34)
