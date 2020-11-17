answer = ''
i = 1
store = []
while answer != 'N':
    answer = input(('Оформим новый товар? ', 'Y/N'))
    if answer == 'Y':
        v = ['название', 'цена', 'колличество', 'ед']
        name = input('Введите название товара: ')
        price = input('Введите цену товара: ')
        quantity = input('Введите колличество товара: ')
        units = input('Введите единицы товара: ')
        l = [name, price, quantity, units]
        zip_dict = dict(zip(v, l))
        zip_number = (i, zip_dict)
        store.append(zip_number)
        i = i + 1
    else:
        pass

for row in store:
    for item in row:
        print(item, end=' ')
    print()


