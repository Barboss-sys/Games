

FED_TAX_RATE = 0.05
REG_TAX_RATE = 0.025

def main():
    print('Программа расчитывает налоги с продаж')
    bay = input_bay()
    fed_tax, reg_tax = all_taxes(bay)

    print(f'На потраченые ${bay:,.2f}\n'
          f'Региональный налог: ${reg_tax:,.2f}\n'
          f'Федератьный налог ${fed_tax:,.2f}\n'
          f'Общий налог ${(fed_tax + reg_tax):,.2f}\n'
          f'Общая сумма продаж ${(bay + reg_tax + fed_tax):,.2f}')

def input_bay():
    bay_count = float(input('Введите стоитмость покупки: '))
    return bay_count

def all_taxes(bay):
    fed_tax = fed_taxe(bay)
    reg_tax = reg_taxe(bay)
    return fed_tax, reg_tax

def fed_taxe(bay):
    fed_tax = bay * FED_TAX_RATE
    return fed_tax

def reg_taxe(bay):
    reg_tax = bay * REG_TAX_RATE
    return reg_tax



main()




