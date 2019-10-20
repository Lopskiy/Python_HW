import sys

p1 = float(sys.argv[1])
p2 = float(sys.argv[2])
p3 = float(sys.argv[3])


def payday(a, b, c):
    s = ((a * b) + c)
    print('Выработка в часах сотрудника составляет ', a, 'часов')
    print('Ставка в час сотрудника составляет = ', b, 'р.')
    print('Пермия сотрудника составляет = ', c, 'р.')
    print('Зароботная плата сотрудника составляет = ', s, 'р.')


payday(p1, p2, p3)
