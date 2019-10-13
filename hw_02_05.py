my_list = [7, 5, 3, 3, 2]
print('Рейтинг ', my_list)
my_list.append(int(input('Введите число рейтинга: ')))
print("Обновленный рейтинг", sorted(my_list, reverse=True))
