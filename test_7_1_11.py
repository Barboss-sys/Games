
"""
Программа принимает в качестве аргумента матрицу со случайными числами числами 
и проверяет евляется ди матрица квадратом Ло Шу
"""



import random

ROWS = 3
COLS = 3

#lo_shu_squaer = [[4, 9, 2],[3, 5, 7],[8, 1, 6]]     ----- введено для теста


def main():
    matrix_lo_shu = create_matrix()
    #matrix_lo_shu = lo_shu_squaer     ------ введено для теста
    print(matrix_lo_shu)
    if (matrix_lo_shu[0][0] + matrix_lo_shu[0][1] + matrix_lo_shu[0][2] == 15
        and matrix_lo_shu[1][0] + matrix_lo_shu[1][1] + matrix_lo_shu[1][2] == 15
        and matrix_lo_shu[2][0] + matrix_lo_shu[2][1] + matrix_lo_shu[2][2] == 15
        and matrix_lo_shu[0][0] + matrix_lo_shu[1][0] + matrix_lo_shu[2][0] == 15
        and matrix_lo_shu[0][1] + matrix_lo_shu[1][1] + matrix_lo_shu[2][1] == 15
        and matrix_lo_shu[0][2] + matrix_lo_shu[1][2] + matrix_lo_shu[2][2] == 15
        and matrix_lo_shu[0][0] + matrix_lo_shu[1][1] + matrix_lo_shu[2][2] == 15
        and matrix_lo_shu[0][2] + matrix_lo_shu[1][1] + matrix_lo_shu[2][0] == 15
    ):

        print(f'Это кватрат Ло Шу !!!')
    else:
        print('Это не квадрат Ло Шу попытайтесь еще раз!!!')



def create_matrix():
    matrix_lo_shu = [[r * c for c in range(COLS)]for r in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            matrix_lo_shu[r][c] = random.randint(1, 9)

    return matrix_lo_shu



if __name__ == '__main__':
    main()




