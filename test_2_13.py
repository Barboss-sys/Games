

years = int(input('Введите колличество лет: '))
tottal_precipitation = 0

print('года\tосадки в мм')
print('-----------------------')

for i in range(years + 1):
    for n in range(1, 13):
        precipitation_p_m = float(input('Введите кол-во осадков в мм: '))
        tottal_precipitation += precipitation_p_m
        precipitation = (tottal_precipitation / 12) * years

print(f'средняя кол-во осадков за весь периуд {precipitation}')
print(f'Среднее кол-во осадков в месяц в мм {tottal_precipitation}')

