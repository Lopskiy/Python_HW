from functools import reduce

my_list = [i for i in range(99, 1001) if i % 2 == 0]
print(my_list)
sum_all = reduce(lambda a, b: a + b, my_list)

print(sum_all)