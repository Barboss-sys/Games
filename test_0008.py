
"""
Программа генерирует вложенные списки
"""

ROWS = 5
COLS = 3

def main():
    matrix = []
    for r in range(ROWS):
        cols_list = []
        for c in range(COLS):
            cols_list.append(r * c)
        matrix.append(cols_list)

    print(matrix)


if __name__ == '__main__':
    main()


"""
matix = [[r * c for c in range(x)] for r in range(y)]
пример лист комприхеншен
"""
