
print('Программа определяет високосный год или нет')
year = int(input('Введите год: '))

if year % 400 == 0 and year % 100 == 0 and year % 4 == 0:
    print(f'В {year} году в феврале 29 дней')
else:
    print(f' В {year} году в феврале 28 дней')