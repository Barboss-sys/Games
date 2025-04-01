import matplotlib.pyplot as plt
"""
Программа считывает ффайл и стороит граффик
"""


def main():
    cost_week = read_file()
    left_edges_full, len_edges = left_edges(cost_week)
    hieght_full = heights()
    month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    bar_width = 1
    print(len(left_edges_full))
    
    plt.bar(len_edges, cost_week, bar_width, color='m')
    plt.title('Граффик еженедельных цен на бензин за 1994г.')
    plt.xlabel('Месяцы 1994 года')
    plt.ylabel('Цены на бензин')
    plt.xticks(left_edges_full, month)
    plt.yticks( )
    
    plt.show()

def read_file():
    outfile = open('1994_Weekly_Gas_Averages.txt', 'r')
    cost_week = outfile.readlines()
    outfile.close()
    index = 0
    while index < len(cost_week):
        cost_week[index] = float(cost_week[index].rstrip('\n'))
        index += 1
    return cost_week

def left_edges(cost_week):
    left_edges_full = []
    len_edges = []
    for i in range(0, 120, 10):
        left_edges_full.append(i)

    for c in range(len(cost_week)):
        len_edges.append(c)
    return left_edges_full,  len_edges

def heights():
    height_full = []
    
    return height_full


if __name__ == '__main__':
    main()



