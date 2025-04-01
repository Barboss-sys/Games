


students1_answers = ['A', 'C', 'A', 'A', 'D',
                   'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D',
                   'C', 'B', 'B', 'D', 'A']


def main():
    outfile = open('stu_answers.txt', 'w')
    for i in students1_answers:
        outfile.write(f'{i}\n')
    outfile.close()

if __name__ == '__main__':
    main()

