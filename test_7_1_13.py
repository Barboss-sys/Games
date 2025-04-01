"""
Генерация простых чисел
программа просит пользователя ввести число > 2
затем выводит все простые числа которые <= введеному числу
"""

def main():
    sample = []
    composite = []
    responses = get_input()
    user_nums = create_num_list(responses)
    for i in user_nums:
        if test_nums(i):
            sample.append(i)
        else:
            composite.append(i)
    print(f'В числовой последовательности\n',
          f'от 2х до {responses} \n'
          f'простых чисел {len(sample)}\n',
          f'{sample}\n'
          f'составных чисел {len(composite)}\n',
          f'{composite}')


def get_input():
    responses = int(input('Введите число: '))
    return responses

def create_num_list(arg):
    user_nums = []
    for i in range(2, arg + 1):
        user_nums.append(i)
    return user_nums

def test_nums(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False   
    return True


if __name__ == '__main__':
    main()

