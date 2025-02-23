

cost_semm = 145000
tax_up = 0.03

print('Плата за симестер')
print('год\tстоимость')
print('======================================')
for i in range(1, 6):
    tax = cost_semm * tax_up
    cost_semm += tax
    print(f'{i}  ---  {cost_semm:,.2f}')
