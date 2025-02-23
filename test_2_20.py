

number = int(input('Введите число: '))

print('вычисляем факториал числа')

for i in range(1, number):
    number *= i

    print(f'Факториал числа = {number:,.2f}')

