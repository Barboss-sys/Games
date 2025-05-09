import matplotlib.pyplot as plt

def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords, marker='D')

    plt.title('Продажи с разбивкой по годам')

    plt.xlabel('Год')
    plt.ylabel('Обьемы продаж')

    plt.xticks(
        [0, 1, 2, 3, 4],
        ['2016', '2017', '2018', '2019', '2020']
    )
    plt.yticks(
        [0, 1, 2, 3, 4, 5],
        ['$0m', '$1m', '$2m', '$3m', '$3m', '$5m']
    )

    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    main()



