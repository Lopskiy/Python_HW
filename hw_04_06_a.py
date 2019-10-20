from itertools import count

a = int(input('Введите первое число: '))

for i in count(a):
    print(i)
    if i > 100:
        break
