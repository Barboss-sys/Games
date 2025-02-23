

mass_pak = int(input('Введите массу груза: '))

if mass_pak < 200:
    print('Стоимость доставки 150 рублей')

elif mass_pak > 200 and mass_pak < 600:
    print('Стоимость доставки 300 рублей')

elif mass_pak > 600 and mass_pak < 1000:
    print('Стоимость доставки 400 рублей')

elif mass_pak > 1000:
    print('Стоимость доставки 475 рублей')