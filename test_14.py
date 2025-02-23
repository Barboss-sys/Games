

mass = int(input('Введите массу тела в кг.: '))
lenth = int(input('Введите рост в см. : '))

imt = mass / (lenth / 100) ** 2

if imt < 18.5:
    print(f'Вы весите меньше нормы {imt}')

elif imt > 18.5 and imt < 25:
    print(f'У вас оптимальный вес {imt}')

elif imt > 25:
    print(f'У вас избыточная массы тела {imt}')

