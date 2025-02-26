
""""
Программа переводит Футы в дюймы
"""
DUIM = 12

def main():
    result_1 = get_input()
    result = calc_duim(result_1)
    print('ФУТЫ\tДюймы')
    print('================')
    print(f'{result_1} ===> {result}')

    

def get_input():
    in_put = int(input('Введите кол-во футов: '))
    return in_put

def calc_duim(arg):
    result = arg * DUIM
    return result

main()


