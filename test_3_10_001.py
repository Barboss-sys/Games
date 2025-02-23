

BASE_HOURS = 40 # Базовые часы в неделю
OT_MULTIPLIER = 1.5 # Коэфицент сверхурочного времяни
TAXES_RATE = 0.13 # налоговая ставка
BONUS = 0.15 # процент пособия




# вызывает пять других функций
def main():
    get_input()
    hours, pay_rate = get_input()
    calc_overtime()
    overtime_pay = calc_overtime(hours, pay_rate)
    calc_gross_pay()
    gross_pay = calc_gross_pay(pay_rate, overtime_pay)
    calc_witholdings()
    taxes, bonus_s = calc_witholdings(gross_pay)
    calc_net_pay()
    net_pay = calc_net_pay(gross_pay, taxes, bonus_s)
    print(f'Ваша заработная плата состовляет: ${net_pay:,.2f}')




#1 получить входные данные
def get_input():
    get_hourly_rate()
    hours = get_hours_worked()
    get_hours_worked()
    pay_rate = get_hourly_rate()
    return hours, pay_rate

#1 получить отработанные часы
def get_hours_worked():
    hours = float(input('Введите кол-во отработанных часов: '))
    return hours
#1 получить ставку опла­ты труда
def get_hourly_rate():
    pay_rate = float(input('Введите почасовую ставку оплаты труда: '))
    return pay_rate


# рассчитать заработную плату до удержаний
def calc_gross_pay(pay_rate, overtime_pay):
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
    return gross_pay


# рассчитать сверхурочные
def calc_overtime(hours, pay_rate):
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER
    return overtime_pay


#2 рассчитать удержания
def calc_witholdings(gross_pay):
    calc_taxes()
    taxes = calc_taxes(gross_pay)
    calc_benets()
    bonus_s = calc_benets(gross_pay)
    return taxes, bonus_s


#2 рассчитать налоги
def calc_taxes(gross_pay):
    taxes = gross_pay * TAXES_RATE
    return taxes
#2 рассчитать пособия
def calc_benets(gross_pay):
    bonus_s = gross_pay * BONUS
    return bonus_s


# рас­считать зарплату на руки
def calc_net_pay(gross_pay, taxes, bonus_s):
    net_pay = (gross_pay - taxes) - bonus_s
    return net_pay



main()


