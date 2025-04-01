import random

ROWS = 3
COLS = 4

def main():
    matrix = list1()
    result = list2(matrix)
    for value in result:
        print(f'Все числа в матрице: {value}')

def list1():
    matrix_list = [[r * c for c in range(COLS)] for r in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            matrix_list[r][c] = random.randint(1, 100)
    return matrix_list

def list2(arg_list):
    result = []
    for i in arg_list:
        for c in i:
            result.append(c)
    return result


if __name__ == '__main__':
    main()
