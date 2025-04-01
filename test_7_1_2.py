import random


r_numbers = []

def main():
    for c in range(7):
        r_numbers.append(random.randint(0, 9))

    for i in r_numbers:
        print(i)


if __name__ == '__main__':
    main()



