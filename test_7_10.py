

ROWS = 5
COLS = 3

duble_lists = [[r * c for c in range(COLS)] for r in range(ROWS)]
for r in range(ROWS):
    for c in range(COLS):
        duble_lists[r][c] = int(input('Введите число: '))


print(duble_lists)
