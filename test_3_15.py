
"""
Программа для расчета калорий
"""
def main():
    fats, carbo = gramms()
    kall_fats, kall_carbo = all_calc(fats, carbo)
    print(f'Жиры: {fats:,.2f} г. == {kall_fats:,.2f} Калорий')
    print(f'Углеводы: {carbo:,.2f} г. == {kall_carbo} Калорий')
    


def gramms():
    fats = eating_fats()
    carbo = eating_carbo()
    return fats, carbo

def eating_fats():
    fats = float(input('Введите кол-во жиров: '))
    return fats

def eating_carbo():
    carbo = float(input('Введите кол-во углеводов: '))
    return carbo

def all_calc(fats, carbo):
    kall_fats = fats * 9
    kall_carbo = carbo * 4
    return kall_fats, kall_carbo



main()

