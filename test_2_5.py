

sum_1 = 0
sum_2 = 31

for i in range(1, 31):
    sum_1 += 1
    #sum_1 += sum_1
    print(sum_1)
    sum_2 -= 1
    print(sum_2)
    summa = (sum_1 / sum_2) + (sum_2 / sum_1)
print(summa)



