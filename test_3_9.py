

CONST_MILL = 0.6214

def main():
    print('Конвертирует километры в мили')
    mills = int(input('Введите километры: '))
    print(f'{mills} км ====> {convert(mills):,.2f} миль')


def convert(arg):
    return arg * CONST_MILL


main()