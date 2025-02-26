
"""
Будущий баланс вклада
"""

EARS_DAY = 365


def main():
    balance, procent, days = get_input()
    result = calc_balance(balance, procent, days)
    print(f'При процентной ставке в {procent}\n'
          f'по прошествии {days} дней\n'
          f'на вашем счете будет {(balance + result):,.2f} р.')


def get_input():
    balance = get_balance()
    procent = get_procent_p_m()
    month = get_months()
    return balance, procent, month

def get_balance():
    balance = float(input('Введите текуший баланс: '))
    return balance

def get_procent_p_m():
    procent = float(input('Введите процентную ставку: '))
    return procent

def get_months():
    days = int(input('Введите кол-во дней: '))
    return days

def calc_balance(balance, procent, days):
    f = (balance * procent * days / EARS_DAY) / 100
    return f
    


if __name__ == '__main__':
    main()


