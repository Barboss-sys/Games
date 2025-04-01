

precipitation = []



def main():
    data = get_input()
    sum_data = calc_precipitation(data)

    print(f'Среднее значение осадков зп год = {sum_data:,.2f}')
    print(f'Минимальное колличество осадков за год = {min(data):,.2f}')
    print(f'Максимальное колличество осадков за год = {max(data):,.2f}')
    print(f'колличество месяцев = {len(precipitation)}')


def get_input():
    try:
        for i in range(12):
            inputing = float(input('Введите кол-во оадков за месяц: '))
            precipitation.append(inputing)
    except ValueError:
        print('Ошибка, значение не может быть NONE')


    return precipitation

def calc_precipitation(arg):
    calc_data = 0
    for i in precipitation:
        calc_data += i
    result = calc_data / len(precipitation)
    return result


if __name__ == '__main__':
    main()

