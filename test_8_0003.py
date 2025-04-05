
"""
метод split 
"""

def main():
    my_string = 'Один два три четыре'
    word_list = my_string.split()
    print(word_list)


if __name__ == '__main__':
    main()


def main():
    data_string = '12/04/2021'
    lata_list = data_string.split('/')
    print(f'День {lata_list[0]}')
    print(f'Мeсяц {lata_list[1]}')
    print(f'Год {lata_list[2]}')


if __name__ == '__main__':
    main()

