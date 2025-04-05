"""
Программа принимает имя, вамилию ,
индефикационный номер в качестве 
аргументов. 
Она возвращает имя для входа в сиситему
login.py
"""

def get_login_name(first, last, idnumber):
    set1 = first[0:3]
    set2 = last[0:3]
    set3 = idnumber[-3:]
    login_name = set1 + set2 + set3
    return login_name

def valid_password(arg):
    password = ''
    for i in arg:
        password += i
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(password) >= 7:
        correct_length = True
        for item in password:
            if item.isupper():
                has_uppercase = True
            if item.islower():
                has_lowercase = True
            if item.isdigit():
                has_digit = True
        if correct_length and has_uppercase and \
            has_lowercase and has_digit:
            is_valid = True
    else:
        is_valid = False
    return is_valid

def main():
    first = input('Введите имя: ')
    last = input('Введите фамилию: ')
    idnumber = input('Введите свой индефикационный номер: ')
    password = get_login_name(first, last, idnumber)
    if valid_password(password):
        print(f'Ваш пароль {password} допустим.')
    else:
        print(f'Ваш {password} пароль не допустим')


if __name__ == '__main__':
    main()
