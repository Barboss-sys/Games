import random

lists = []

def main():
    data = lists_gen()
    outfiles = open('charge_accounts.txt', 'w')

    for i in data:
        outfiles.write(f'{str(i)}\n')

    outfiles.close()
    

def lists_gen():
    for i in range(5):
        lists.append(random.randint(999999, 9999999))
    return lists



if __name__ == '__main__':
    main()


