
"""
программа для сохранения спискового значения в файл V2.0
"""

def main():
    cities = ['moscow', 'khabarovsk', 'ircutsk', 'tambov']

    outfile = open('cities.txt', 'w')
    for i in cities:
        outfile.write(f'{i.title()}\n' )

    outfile.close()

if __name__ == '__main__':
    main()