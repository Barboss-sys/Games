

time = int(input('Введите время в пути: '))
speed = int(input('Введите скорость: '))
total = 0


print('Час\tПройденное расстояние')
print('----------------------------------')
for i in range(1, time + 1):
    total += speed

    print(f'{i}\t{total}')



