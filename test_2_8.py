

number = int(input('Введите число в диапазоне от 1 до 100: '))

while number not in range(1, 100):
    print('Ошибка!!!')
    number = int(input('Введите число еще раз: '))

    