

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#for i in list1:
#    list2.append(i ** 2)

list2 = list(i ** 2 for i in list1)

print(list2)
