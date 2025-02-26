



def main():
    print('Программа подсчета сидячих мест')
    total = chanch_spot()
    col_income = calc_b(total)
    print(f'общий доход от проданных билетов ${col_income:,.2f}')


def chanch_spot():
    print('Для выхода нажмите "z"')
    spotss = []
    total = []
    while 'z' not in spotss:
        spot = input('Введите категорию сидячего места A / B / C: ')
        if spot == 'a' or spot =='A':
            total += spot
        elif spot == 'b' or spot == 'B':
            total += spot
        elif spot == 'c' or spot == 'C':
            total += spot
        elif spot == 'z' or spot == 'Z':
            spotss.append('z')
            print('ВЫХОД!!!!')
        else:
            print('Недопустимое значение!!!!')
    return total

def spots(spot):
    if spot == 'a' or spot == 'A':
        price_b = 20
    elif spot == 'b' or spot == 'B':
        price_b = 15
    else:
        price_b = 10
    return price_b

def calc_b(total):
    income = 0
    for i in total:
        income += spots(i)
    return income


main()

