import random

"""
Программа генерирует 100 случайных чисел и проверяет и на четность
"""

def main():
    count = gen_nums()
    result, result_1 = parity_determin(count)
    print('из 100 случайно сгенерированных чисел:\n'
          f'Четных - {result}\n'
          f'Нечетных - {result_1}')

def gen_nums():
    count = []
    for i in range(101):
        x = random.randint(1, 100)
        count.append(x)
    return count

def parity_determin(count):
    result = 0
    result_1 = 0
    for i in count:
        if i % 2 == 0:
            result += 1
        else:
            result_1 += 1
    return result, result_1


main()


