

"""
Программа считывает данные из файла
показывает:
1. среднегодовое изменение ччисленности населения
2. год с наиьольшем увелечением численности
3. год с наименьшей численностью населения

"""

def main():
    population = read_file()
    year_population = creat_list(population)
    input_data = get_input()
    result = seach_data(input_data, year_population)
    keys = list(year_population.keys())
    index1 = list(year_population.values()).index(min(population))
    index2 = list(year_population.values()).index(max(population))
    min_res = keys[index1]
    max_res = keys[index2]
    print('Среднегодовое изменение населения за определенный периуд')
    print(f'Периуд --- {input_data}\tчисленность  {result}')
    print(f'Год с наименьшей популяцией - {min_res}')
    print(f'Год с наибольшей популяцией - {max_res}')


def read_file():
    outfile = open('USPopulation.txt', 'r')
    population = outfile.readlines()
    outfile.close()
    index = 0
    while index < len(population):
        population[index] = population[index].rstrip('\n')
        population[index] = int(population[index])
        index += 1
    return population


def creat_list(population):
    year_population = {}
    years = list(range(1950, 1991))
    for i in range(0, len(years)):
        year_population[years[i]] = population[i]
    return year_population

def get_input():
    input_data = int(input('Введите год: '))
    return input_data

def seach_data(input_data, year_population):
    if input_data in year_population:
        return year_population[input_data]




if __name__ == '__main__':
    main()




