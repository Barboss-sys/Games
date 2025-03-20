

def main():
    numbers_1 = int(input('введите число: '))

    numbers = open('numbers_1.txt', 'a')

    for i in range(1, int(numbers_1) + 1):
        print(f'Введите данные о сотруднике: ')

        name = input('Имя: ')

        id_num = input('Индефикационнный номер: ')

        dept = input('Отдел: ')


        numbers.write(f'{str(name)}\n')
        numbers.write(f'{str(id_num)}\n')
        numbers.write(f'{str(dept)}\n')

        numbers.close()
        

if __name__ == '__main__':

    main()

