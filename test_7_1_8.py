
"""
Программа считывает имена из файлов и записывает в списки
дает возможность юзеру ввести имя / имена 
проверяет есть ли эти имена в списках 
выводит ответ с подтвирждением или опровержением запроса
"""

def main():
    boy_names = read_file_boy_names()
    girl_names = read_file_girl_names()
    full_names = boy_names + girl_names
    names = get_input()
    result = testing_name(full_names, 
                          names)
    print(full_names)
    print(result.title())


def read_file_boy_names():
    outfile1 = open('BoyNames.txt', 'r')
    boy_names = outfile1.readlines()
    outfile1.close()
    index = 0
    while index < len(boy_names):
        boy_names[index] = boy_names[index].rstrip('\n').lower()
        index += 1
    return boy_names

def read_file_girl_names():
    outfile1 = open('GirlNames.txt', 'r')
    girl_names = outfile1.readlines()
    outfile1.close()
    index = 0
    while index < len(girl_names):
        girl_names[index] = girl_names[index].rstrip('\n').lower()
        index += 1
    return girl_names

def get_input():
    again = 'y'
    names = []
    while again == 'y':
        input_name = input('Введите имя: ')
        names.append(input_name)
        print('Хотите ввести еще имя?')
        again = input('y = да / n = нет: ')
    return names

def testing_name(full_name, arg):
    for i in arg:
        if i in full_name:
            answer = 'Имя находятся в списке !'
        
        else:
            answer = 'Таких имен / имени в списке нет !'

    return answer



if __name__ == '__main__':
    main()


