from lists import names_o
import random


falen_guest = 'alen'
new_guest = 'saymon'
z = names_o.index('alen')
names_o[z] = new_guest

names_o.insert(0, 'Josh')
names_o.insert(3, 'Ben')
names_o.append('max')

print(f'К сожелению {falen_guest.title()} прийти не сможет,'
      f'но сможет прийти {new_guest.title()}')
print('К сожелению новый стол не успевают привезти,\n'
      'на чаепитее места хватит только для двоих\n'
      'заранее прошу прощения')


print('=======================================')
print(f'Длинна списка names_o = {len(names_o)}')
random_guests1 = random.sample(names_o, 2)
for i in random_guests1:
    print(f'Приглашаю на чаепитье дорогой {i.title()}!')

print('=======================================')



while len(names_o) >= 3:
      random_guests = random.choice(names_o)
      index_guest = names_o.index(random_guests)
      names_o.pop(index_guest)
      print(f'{random_guests.title()}, '
            'Прошу прощения, но чаепитье не состаиться,'
            'жду вас с нетерпеньем в следующий раз.')
      
print(f'\nЖду вас в гости {names_o[0].title()}'
      f' и {names_o[1].title()}')
      


del names_o[0]
del names_o[0]

print( names_o)

