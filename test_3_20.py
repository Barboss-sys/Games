
"""
Порограмм для определения максимального значения
IN 2 целочисленных значения
OUT максимальное из принятого
"""

def main():
    in_put, in_put_1 = get_input()
    result = max_answer(in_put, in_put_1)
    print(f'Большее число {result}')
    
def get_input():
    in_put = int(input('Введите первое число: '))
    in_put_1 = int(input('Введите второе число: '))
    return in_put, in_put_1

def max_answer(a, b):
    if a > b:
        result = a
    else:
        result = b
    return result

    
main()


