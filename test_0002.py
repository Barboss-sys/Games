
"""
Программа для расчета заработной платы реализованаая через словарь,
добавлена функция добавления работников
"""


personals = {'antony': 0, 'billy': 0, 'ben': 0,
             'elena': 0, 'clara': 0, 'irina': 0}


def main():
    print('Добавить нового сотрудника?')
    again = input('д = да, н = нет: ')

    while again == 'д':
        name = input(' Введите имя сотрудника: ')
        personals[name] = 0
    
        print('Добавить еще одного сотрудника?')
        again = input('д = да, н = нет: ')

    for name in personals:
        personals[name] = float(input(f' Введите колличество отработанных часов сотрудника {name.title()}: '))

    pay_rate = float(input('Введите по часовую оплату труда: '))

    for keys in personals:
        gross_pay = personals[keys] * pay_rate
        print(f'Заработная плата сотрудника {personals[keys]} = $ {gross_pay:,.2f}')


if __name__ == '__main__':
    main()






