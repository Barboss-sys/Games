

population = int(input('Введите сатртовое колличество: '))
popul_day_up = int(input('Введите среднесуточное увеличение в % : '))
days = int(input('Введите кол-во дней : '))
population_day = 0

print('День\nПопуляция')
for i in range(1, days + 1):
    population_day = population * (popul_day_up / 100)
    population += population_day
    print(f'{i} ---- {population:,.3f}')
