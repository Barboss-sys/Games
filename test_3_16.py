

income = 0
spot = 0

def main():
    print('Программа подсчета сидячих мест')
    chanch_spot()
    #price_b = spots(spot)

    print(f'общий доход от проданных билетов ${price_b}')




def chanch_spot():
    print('Для выхода нажмите "z"')

    while spot != 'z' or 'Z':
        spot = input('Введите категорию сидячего места A / B / C: ')
    #return spot


    #def spots(spot):
        if spot == 'a' or spot == 'A':
            price_b = 20

        elif spot == 'b' or spot == 'B':
            price_b = 15

        elif spot == 'c' or spot == 'C':
            price_b = 10

        elif spot == 'z' or spot == 'Z':
            print('ВЫХОД!!!')

        else:
            print('Не корректные данные!!!')

    return price_b


main()

