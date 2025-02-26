
"""
программа расчета кинетической энергии
"""

def main():
    massa, speed = get_input()
    result = kinetic_energy(massa, speed)
    print(f'Кинетическая энергия равна {result:,.2f} Дж')

def get_input():
    massa = get_massa()
    speed = get_speed()
    return massa, speed

def get_massa():
    massa = int(input('Введите массу обьекта в кг: '))
    return massa

def get_speed():
    speed = int(input('Введите скорость обьекта в м / с: '))
    return speed

def kinetic_energy(massa, speed):
    K_energy = 1 / 2 * massa * speed ** 2
    return K_energy


main()
    