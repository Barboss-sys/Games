
signal_num = 1
sum_num = 0

print('Введате отрицательное число чтобы выйти')
while signal_num > 0:
    signal_num = int(input('Введите число: '))
    sum_num += signal_num
    print(f'сумма = {sum_num}')
    

print(f' сумма всех чисел  =  {sum_num}')

