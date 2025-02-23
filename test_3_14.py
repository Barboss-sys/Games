
COST_RATE = 0.6
TAX_RATE = 0.0072

def main():
    house = input_house()
    cost = cost_house(house)
    result = cost * TAX_RATE
    print(f'Налог на собственность равен ${result:,.2f}')


def input_house():
    house = float(input('Введите стоимость: '))
    return house

def cost_house(house):
    cost = house * COST_RATE
    return cost
    
    
main()



