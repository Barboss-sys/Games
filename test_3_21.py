
"""
Программа расчета высоты падения
"""

G = 9.8

def falling_distance():
    for i in range(1, 10):
        print('время\tрасстояние')
        print('...................')
        print(f'{i}c --->  {calculadet(i):,.2f}m')
        print('====================')

def calculadet(t):
    d = (1 / 2) * G * t ** 2
    return d


falling_distance()