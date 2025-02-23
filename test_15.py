
seconds = int(input('Введите секунды: '))

if seconds >= 60 and seconds <= 3600:
    print(f'{seconds // 60} минут , {seconds % 60} секунд')

elif seconds >= 3600 and seconds <= 86400:
    print(f'{seconds % 60} часов,'
          f'{(seconds // 60) % 60} минут, '
          f'{seconds % 3600} секунд')
    
elif seconds >= 86400:
    print(f'{seconds // 86400} дней,'
          f'{(seconds // 86400) % 24} часов,'
          f'{(seconds // 24) % 60} минут,'
          f'{((seconds // 24) // 60) % 60 } секунд')
    
else:
    print(f'{seconds} секунд')
    

