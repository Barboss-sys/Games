
"""
Программа сохраняет список чиcел в файл
"""

def main():
    numbers = []
    for i in range(11):
        numbers.append(i)

    outfile = open('number_list.txt', 'w')

    for i in numbers:
        outfile.write(f'{str(i)}\n')

    outfile.close()

if __name__ == '__main__':
    main()

