
"""
программа для проверки ответов на экзамене

"""

correct_answers = ['A', 'C', 'A', 'A', 'D',
                   'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D',
                   'C', 'B', 'B', 'D', 'A']
students_answers = ['A', 'C', 'A', 'A', 'D',
                   'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D',
                   'C', 'B', 'B', 'D', 'A']


def main():
    outfile = open('cor_answers', 'w')
    for i in correct_answers:
        outfile.write(f'{i}\n')
    outfile.close()

    student_data = read_stu_answers()
    true_score, failscore, numb_answer = testing_answers(student_data, correct_answers)

    if true_score < 15:
        print('Вы не сдали экзамен.')
    else:
        print('Поздравляю вы сдали экзамен !!!')

    print(f'На экзамене было  {len(correct_answers)}')
    print(f'из {len(correct_answers)} вы дали {true_score} правельных ответов')
    print(f'не правильных ответов было {failscore}')
    print(f'номера не правильных ответов {numb_answer}')



def read_stu_answers():
    infile = open('stu_answers.txt', 'r')
    stu_answers = infile.readlines()
    infile.close()
    index = 0
    while index < len(stu_answers):
        stu_answers[index] = stu_answers[index].rstrip('\n')
        index += 1
        
    return stu_answers


def testing_answers(student_data, correct_answers):
    true_score = 0
    faile_score = 0
    num_answer = []
    for i in range(len(correct_answers)):
        if student_data[i] == correct_answers[i]:
            true_score += 1
            
        else:
            faile_score += 1
            num_answer.append(i + 1)

    return true_score, faile_score, num_answer


if __name__ == '__main__':
    main()









