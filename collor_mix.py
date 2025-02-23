print('программа для смешивания цветов!!!')
print('можно смешивать только Красный, Желтый и Зеленый цвета')
colors = 'красный', 'желтый', 'синий'

color_1 = input('введите цвет: ')
color_2 = input('введите цвет: ')
if color_1 in colors or color_2 in colors:
    if (color_1 == colors[0] or color_1 == colors[2]) and (color_2 == colors[0] or color_2 == colors[2]):
        print('получается - ФИОЛЕТОВЫЙ !!!')

    elif (color_1 == colors[0] or color_1 == colors[1]) and (color_2 == colors[0] or color_2 == colors[1]):
        print('получается - ОРАНЖЕВЫЙ !!!')

    elif (color_1 == colors[1] or color_1 == colors[2]) and (color_2 == colors[1] or color_2 == colors[2]):
        print('получается - ЗЕЛЕНЫЙ !!!')
    

else:
    print('не корректный цвет!')

