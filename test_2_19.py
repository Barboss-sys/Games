

kall = 500
mass_per_month = 1.5
months = 7
massa = int(input('Введите массу тела: '))



print('Если вы будите придерживаться диеты ')
print('Ваш вес будет таким')
print('Месяц\tВес')
for i in range(1, months + 1):
    massa -= mass_per_month
    print(f'{i} ---- {massa:.2f}')


