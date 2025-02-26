
"""
Программа для расчета среднего бала и уровня знаний
"""
def main():
    print('Программа для расчета уровня знаний ')
    answer = get_input()
    med_ball = calc_average(answer)
    result = determine_grade(med_ball)
    print(f'Уровень ваших знаний равен {result}')


def get_input():
    ansers = []
    print('Введите 5 оценок в 100 бальной шкале')
    for i in range(6):
        x = int(input('Введите оценку: '))
        ansers.append(x)
    return ansers

def calc_average(answer):
    med_ball = 0
    sum_ball = 0
    for i in answer:
        sum_ball += i
    med_ball = sum_ball / len(answer)
    return med_ball


def determine_grade(med_ball):
    if med_ball > 90:
        result = 'A'
    elif med_ball >= 80 and med_ball <= 89:
        result = 'B'
    elif med_ball >= 70 and med_ball <= 79:
        result = 'C'
    elif med_ball >=60 and med_ball <= 69:
        result = 'D'
    elif med_ball < 60:
        result = 'F'
    return result


main()

