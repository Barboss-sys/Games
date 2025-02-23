import random

again = 'д'
MIN = 1
MAX = 6


while again.lower() == 'д':
    print('Бросаем кубики ...')
    print('Значение граней:')
    print(random.randint(MIN, MAX))
    print(random.randint(MIN, MAX))
    print(random.randint(MIN, MAX))
    print(random.randint(MIN, MAX))
    print(random.randint(MIN, MAX))

    again = input('Бросить кубики еще раз (д = да): ')

