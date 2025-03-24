

list1 = list(range(101))

list2 = list(i for i in list1 if i % 2 == 0)

print(f' ++++++++++++++++\n {list1}')
print(f' ==================\n{list2}')