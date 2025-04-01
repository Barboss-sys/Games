"""
Программа считывает данные из файла
записывает их в список
простик пользователя ввести вопрос 
и выдает ему случайны ответ из списка
-------------------------------------
MAGIC BALL
"""
import random

def main():
    questions = get_input()
    magic_answer = read_file()
    x = random.randint(0, len(magic_answer))
    print(f'На ваш вопрос {questions}\n',
          f'великий магический шар дал ответ \n',
          f'{magic_answer[x]}')


def read_file():
    outfile = open('8_ball_responses.txt', 'r')
    magic_answer = outfile.readlines()
    outfile.close()
    index = 0
    while index < len(magic_answer):
        magic_answer[index] = magic_answer[index].rstrip('\n')
        index += 1

    return magic_answer

def get_input():
    question = input('Введите интересующий вас вопрос: ')
    return question


if __name__ == '__main__':
    main()

    