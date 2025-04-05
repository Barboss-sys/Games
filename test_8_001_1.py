import test_8_001 as tes

def main():
    password = input('Введите пароль: ')
    
    while not tes.valid_password(password):
        print('Этот пароль не допустим!')
        password = input('Введите свой пароль: ')

    print('Этот пароль допустим.')

if __name__ == '__main__':
    main()

    