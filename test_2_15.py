


zp_p_d = int(input('Введите кол-во дней: '))
total_zp = 1

print('Итоговая ЗП в Рублях за весь период')
for  i in range(1, zp_p_d + 1):
    total_zp += total_zp
    total_zp_p = total_zp / 100

    print(f'{i} доход  --- === >  {total_zp:.2f}')

print(f' Общий доход в рублях {total_zp_p:.2f}')


