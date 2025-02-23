
"""
Программа расчитывает расходы на машину
"""

def main():
    print('Расходы на машину')
    expens = expenses()
    print('месяц\t\tгод')
    print(f'{expens:,.2f} ==== {(expens * 12):,.2f}')


def expenses():
    expens = float(input('Введите месячные расходы: '))
    return expens


main()