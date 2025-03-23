
"""
Эта программа считывает числа из файла в список
"""

def main():
    infile = open('number_list.txt', 'r')
    numbers = infile.readlines()
    infile.close()

    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    print(numbers)



if __name__ == '__main__':
    main()

