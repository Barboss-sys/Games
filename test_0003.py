
"""
Программа для вычисления откорректированной средне арифмитической оценки
"""

def main():
    score = get_score()
    total = get_total(score)
    lower = min(score)
    total -= lower
    end_total = total / (len(score) - 1)
    print(f'Скорректированная среднеарифмитическая оценка = {end_total:,.2f}')

def get_score():
    again = 'д'
    score_list = []

    while again == 'д':
        score = int(input('Введите оценку: '))
        score_list.append(score)
        print('Хотите добавить еще оценку?')
        again = input('д = да / н = нет : ')

    return score_list


def get_total(score_list):
    total = 0
    for i in score_list:
        total += i
    return total



if __name__ == '__main__':
    main()

