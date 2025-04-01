

sales = []

def main():
    again = 'д'
    while again == 'д':
        sale_per_day = float(input('Введпте сууму продаж за день: '))
        sales.append(sale_per_day)
        print('Ввести еще продажу')
        again = input('д = да / н = нет: ')

    print(f'Сумма продаж за неделю = {sum(sales)}')



if __name__ == '__main__':
    main()


