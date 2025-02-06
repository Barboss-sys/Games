

PERSONAL_DATA = []

def data_collector():
    name_data = {}

    name = input('Ваше имя : ')
    name_data[name] = name
    addres = input('адрес: ')
    name_data[addres]= addres
    phone = input('номер телефона: ')
    name_data[phone]= phone
    proff = input('ваша профессия: ')
    name_data[proff]= proff

    PERSONAL_DATA.append(name_data)


data_collector()

