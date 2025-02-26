
"""
Программа выводит все простые числа в диапазоне от 1 до 100
"""

def main():
    count = gen_num()
    print(f'Все простые числа в диапазоне от 1 до 100')
    for i in count:
        if i >= 2:
            print(f'{i}')
    

def gen_num():
    count = []
    for i in range(1, 101):
        x = is_prime(i)
        count.append(x)
    return count

def is_prime(num):
    if num <= 1:
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return num


if __name__ == '__main__':
    main()
