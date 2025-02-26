import random

"""
Игра Угадай число 
"""
quiting_1 = 'да'

def main():
    print('Угадай число с 10 попыток')
    counter = 10
    if counter < 10 or counter > 0:
        number = gen_num()
    
    quiting_1 = 'д'
    while quiting_1 == 'д' or quiting_1 == 'Д':
        answer = get_input()
        
        if counter > 0:
            counter -= 1
            print(counter)
        else:
            counter = 10
            print('Вы проиграли ! , кончались попытки')
            print('Съиграем еще раз ?, да (д)/ нет(н): ')
            quiting_1 = input('')
            
        if answer == number:
            print('Поздравляю вы угадали !!!')
            print('Съиграем еще раз ?, да (д)/ нет(н): ')
            quiting_1 = input('')
        elif answer > number:
            print('Слишком много попробуйте еще раз.')
        elif answer < number:
            print('Слишком мало попробуйте еще раз.')
        else:
            print('Недопустимое значение.')


def get_input():
    answer = int(input('Введите число: '))
    return answer

def gen_num():
    num_gen = random.randint(1, 100)
    return num_gen


if __name__ == '__main__':
    main()

