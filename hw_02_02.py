my_list = [2, 2.53, 'Number', [1, 2, 2], True, False, [77, 87]]
print('Элементы списка my_list', my_list)

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
