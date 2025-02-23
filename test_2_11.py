

month_balans = int(input('Введите сумму на один месяц: '))

expenses = 0

for i in range(31):
    expenses_day = float(input('Введите расходы за день: '))
    expenses += expenses_day
    print(expenses)
    result = month_balans - expenses

print(f'На вашем балансе осталось {result}$')


