
sosiski_pak = 10
bylki_pak = 8

persons = int(input('Сколько гостей: '))
hot_dogs = int(input('по сколько хот-догов: '))


hot_dog = persons * hot_dogs

need_sosiski = hot_dog / sosiski_pak
need_bylki = hot_dog / bylki_pak

min_sos = hot_dog % sosiski_pak
min_bylk = hot_dog % bylki_pak

print(f'минимум сосисок {need_sosiski}')
print(f'минимум булок {need_bylki}')
print(f'остаток сосисок {min_sos}')
print(f'остаток булок {min_bylk}')


