import random

nums = []

def main():
    int_nums = get_input()
    sum_nums = calc_nums(int_nums)

    print(f'Наименьшее число = {min(nums)}')
    print(f'Наибольшее число = {max(nums)}')
    print(f'Сумма чисел в списке = {sum_nums}')
    print(f'Среднеарифметическое значение = {sum_nums / len(nums):,.2f}')



def get_input():
    try:
        for i in range(21):
            input_nums = float(input('Введите случайное число: '))
            nums.append(input_nums)
    except ValueError:
        print('Значение не может быть NONE')

    return nums

def calc_nums(arg):
    total = 0
    for i in arg:
        total += i

    return total


if __name__ == '__main__':
    main()



