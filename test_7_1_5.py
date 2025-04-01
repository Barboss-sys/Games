

"""
Написать программу которая будет 
проверять допустимость номера 
(находится ли он в файле)
прога должна :
1. выгружать файл в список
2. проверять на нахождение в нем номера
3. информировать о наличае или отсутствии
4. предлагать внести номер в случае его отсутствии
5. попросить пользователя ввести номер


"""

def main():
    infiles = open('charge_accounts.txt', 'r')
    list_data = infiles.readlines()
    infiles.close()

    index = 0
    while index < len(list_data):
        list_data[index] = int(list_data[index])
        index += 1

    print(list_data)
    indata = get_input()
    result = test_data(indata, list_data)

    print(result)


def get_input():
    indata = int(input('Введите номер счета: '))
    return indata

def test_data(indata, list_data):
    if indata in list_data:
        result = 'Номер счета найден'
    else:
        result = 'Номер не найден'

    return result


if __name__ == '__main__':
    main()




