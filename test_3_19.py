import random
"""
Программа для обучения сдожению больших чисел
"""

def main():
    x = integ_1()
    y = integ_2()
    print(f'{x}\n\t+\n{y}')
    in_put = get_input()
    result = answers(x, y, in_put)
    print(result)

def get_input():
    in_put = int(input('Введите ответ: '))
    return in_put

def answers(x, y, answer):
    if x + y == answer:
        result = 'Поздравляю вы ответили верно!'
    else:
        result = f'Неверно !!! правильный ответ {x + y}'
    return result
    
def integ_1():
    x = random.randint(1, 10000)
    return x

def integ_2():
    y = random.randint(1, 10000)
    return y


main()



