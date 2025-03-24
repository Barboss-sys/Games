
"""
программа для сохранения спискового значения в файл
"""


def main():
    cities = ['moscow', 'khabarovsk', 'ircutsk', 'tambov']

    outfile = open('cities.txt', 'w')
    outfile.writelines(cities)

    outfile.close()

if __name__ == '__main__':
    main()

