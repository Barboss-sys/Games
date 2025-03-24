
num1 = []
num2 = []
num1 = range(101)

#num2 = num1[:] самы короткий способ скопировать список

for i in num1:
    num2.append(i)

print(f'Cписок 2\n{num2}')