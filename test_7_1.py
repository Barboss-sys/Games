
names =[]
again = 'д'

while again == 'д':
    name = input('Введите имя: ')
    names.append(name)

    print('Добавить еще имя ?')
    again = input('д = да / н = нет: ')

print(names)