import matplotlib.pyplot as plt


def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords)

    plt.title('Образец данных')

    plt.xlabel('Это ось х')
    plt.ylabel('Это ось у')

    plt.xlim(xmin=0, xmax=6)
    plt.ylim(ymin=0, ymax=6)

    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    main()



