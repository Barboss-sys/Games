


MIN_SAVE_RATE = 0.8

def main():
    print('Программа лдя расчета страховки')
    save = save_input()
    save_tax = save * MIN_SAVE_RATE
    print(f'Минимальная сумма страховки {save_tax:,.2f}')
    pass

def save_input():
    save = float(input('Введите стоимость недвижимости: '))
    return save


main()