import random

list1 = []

for i in range(101):
    list1. append(random.randint(10, 300))

print(f'++++++++++\n{list1}')

list2 = list(i for i in list1 if i > 100)

print(f'================={list2}')