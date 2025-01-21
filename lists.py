
"""
Строковый метод удаления пробелов
"""

x = 'python!'
y = '   python!   '
print(
    f' длинна строки x = {len(x)}, а длинна строки у = {len(y)}')

c = len(x) == len(y.strip())  # lstrip() -слева ,rstrip() -справа
print(f'{c}\n{x}\n{y}')


"""
Изменение , Добавление и Удаление в списках
"""

names = ['alen', 'jhon', 'wullam', 'nicolas',]

names[1] = 'marcus'
names.append('stiven')
names.insert(-1, 'albert')

names_o = names[:] # Копирование ( Дублирование) списка

index = names.index('alen')

popped_names = names.pop(-3) # Удаление по индексу
del names[index]

names.remove('wullam')  #Удаление по значению
faike_name = 'marcus'
names.remove(faike_name)


for i in names:
    print(f"Hello my friend {i.title()}")


print(f'By, {popped_names.title()}')
print(f'\n {faike_name.title()} - придуманное имя')


print('\n=========================================')


"""
Упорядочивание спиcка
"""

names.sort()
print(names)
names.sort(reverse=True)
print(names)

print(f'Этот список временно отсортирован {sorted(names)}')
print(f'оригинал списка {names}')

