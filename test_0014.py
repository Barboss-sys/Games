import matplotlib.pyplot as plt

def main():
    values = [20, 60, 80, 40]
    slice_libel = ['I квартал', 'II квартал', 'III квартал', 'IV квартал']


    plt.pie(values, labels=slice_libel, colors=('r', 'g', 'b', 'm', 'k'))
    plt.title('Продажи с разбивкой по кварталам')
    plt.show()



if __name__ == '__main__':
    main()


