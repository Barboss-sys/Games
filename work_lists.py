


pizzas = ['peppironi', 'balonese', 'meat']


for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')

print('I really love pizza!')

animals = ['dog', 'caat', 'lama', 'cow']
for animal in animals:
    print(f'A {animal} would make a great pet')

print('Any of these animals would make a great pet!')


squares = [value**2 for value in range(11)]
print(squares)


numbers = list(range(1_000_000))
for i in numbers:
    print(i)


print(sum(numbers))

n1 = list(range(1, 21, 2))
print(n1)


squaers = [i**2 for i in range(3, 31, 3)]


print(squaers)

cube = [i**3 for i in range(11)]

print(cube)
