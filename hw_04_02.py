my_list = [80, 25, 30, 45, 50]
new_list = []
print(my_list)
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])
print(new_list)
