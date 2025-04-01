import matplotlib.pyplot as plt

def main():
    values = [20, 80, 40, 60, 30, 70]
    label_pays = ['Арккндная плата', 'бензин', 'продукты питания',
                  'одежда', 'платежи по автомашине', 'прочее']
    
    plt.pie(values, labels=label_pays, colors=('m', 'r', 'b', 'g', 'k', 'r'))
    plt.title('Круговая диаграмма расходов')
    plt.show()


if __name__ == '__main__':
    main()





