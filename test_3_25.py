


def main():
    answer = get_input()
    result = is_prime(answer)
    print(f'Введеное число является простым ?: {result}')

def get_input():
    answer = int(input('Введите число: '))
    return answer

def is_prime(num):
    if num <= 1:    # отсикаем отрицательные числа
        return False
    for i in range(2, int(num ** 0.5) + 1): # делим число на все числа от 2
        if num % i == 0:                    # до корня из этого числа
            return False                    # Если делится - число составное!
    return True

if __name__ == '__main__':
    main()

    