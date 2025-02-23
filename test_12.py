
price = 99

coll_bay = int(input('введите колличество купленного товара: '))

if coll_bay > 10 and coll_bay < 19:
    tax = 0.1
    print(f'сумма скидки {price * tax}, сумма покупки {(coll_bay * price) * tax}')
    
elif coll_bay > 20 and coll_bay < 49:
    tax = 0.2
    print(f'сумма скидки {price * tax}, сумма покупки {(coll_bay * price) * tax}')
    
elif coll_bay > 50 and coll_bay < 99:
    tax = 0.3
    print(f'сумма скидки {price * tax}, сумма покупки {(coll_bay * price) * tax}')
    
elif coll_bay > 100:
    tax = 0.4
    print(f'сумма скидки {price * tax}, сумма покупки {(coll_bay * price) * tax}')
    
else:
    print('У вас нет скидки')
    

    
