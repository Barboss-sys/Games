

"""
Чемпионный Мировой Серии:

"""

def main():
    years = create_years_list()
    winner_team = read_file()
    inp_data = get_input()
    win_years = []
    result = []
    if inp_data in winner_team:
        for i in range(len(winner_team)):
            if winner_team[i] == inp_data:
                win_years.append(i)
        #win_years = [i for i in range(len(winner_team)) if winner_team[i] == inp_data]
    for i in win_years:
        result.append(years[i])
    print(f'Команда {inp_data.title()}\n',
          f'становилась чемпионом {len(win_years)} раз\n',
          f'В {result} годах')
    

def read_file():
    outfile = open('WorldSeriesWinners.txt', 'r')
    winner_teams = outfile.readlines()
    outfile.close()
    index = 0
    while index < len(winner_teams):
        winner_teams[index] = winner_teams[index].rstrip('\n').lower()
        index += 1
    return winner_teams


def create_years_list():
    years = []
    for i in range(1903, 2009):
        years.append(i)

    for item in years:
        if item == 1904 or item == 1994:
            years.pop(years.index(item))
    return years


def get_input():
    inp_data = input('Введите название команды: ')
    return inp_data.lower()




if __name__ == '__main__':
    main()

