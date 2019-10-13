my_list = [2, 2.53, 'Number', [1, 2, 2], True]
type_list = []
for i in range(len(my_list)):
    type_list.append(type(my_list[i]))
print('Элементы списка my_list', my_list)
print('Типы элементов списка my_list', type_list)
