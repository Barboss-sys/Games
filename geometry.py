# Эта программа позволяет пользователю выбирать различные
# геометрические вычисления из меню.
# Программа импортирует модули circle и rectangle.
import circle
import rectangle


# Константы для элементов меню.
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# Главная функция.
def main():
    # Переменная choice управляет циклоm
    # и содержит вариант выбора пользователя.
    choice = 0

    while choice != QUIT_CHOICE:
        # Показать меню
        display_menu()

        # Получить вариант выбора пользователя.
        choice = int(input('Выберите вариант: '))

        # Выполнить выбранное действие
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print('Площадь круга равна', circle.area(radius))

        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Введите радиус: '))
            print('Длина окружности равна', 
                  circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длинну прямоугольника: '))
            print('Площадь равна', rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длинну прямоугольника: '))
            print('Периметр равен', rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print('Выходим из системы')
        else:
            print('Ошибка: недопустимый выбор')


# Функция display_menu показыват меню
def display_menu():
    print('МЕНЮ')
    print('1. Площфдь круга')
    print('2. Длина окружности')
    print('3. Площадь прямоугольника')
    print('4. Периметр прямоугольника')
    print('5. Выход')


# Вызвать главную функцию
main()



