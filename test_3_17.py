
"""
Оценщик малярных работ
"""

WORK_TAX = 2000 # в час
WORK_P_H = 1.25 # кв метры на часы = обьем в час


def main():
    square, color_price_p_b = get_input()
    work_h = calc_work_h(square)
    work_per_h = calc_price_w(work_h)
    colors = color_price(square)
    color_cost = color_price_p_b * colors
    all_work_cost = work_per_h + color_cost

    print(f'Кол-во емкаcтей краски {colors:,.2f}')
    print(f'Кол-во затраченых часов {work_h:,.2f}')
    print(f'Стоимость краски {color_cost:,.2f}')
    print(f'Стоимость работ {work_per_h:,.2f}р.')
    print(f'Общая стоитмость работ {all_work_cost:,.2f}р.')


def get_input():
    square = get_square()
    color_price = get_price()
    return square, color_price

def get_square():
    square = float(input('Введите площадь окрашиваемой стены: '))
    return square

def get_price():
    color_price = float(input('Введите стоимость 5-литровой банки краски: '))
    return color_price

def calc_work_h(square):
    work_h = square / WORK_P_H # Делим обьем  на коэф работы в час = часы
    return work_h

def color_price(square):
    colors = square // 10
    return colors

def calc_price_w(work_h):
    work_per_h = work_h * WORK_TAX # получаем стоимость работы
    return work_per_h


main()
