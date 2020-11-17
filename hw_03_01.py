def fraction(p1, p2):
    try:
        p1 / p2
    except ZeroDivisionError:
        while p2 == 0:
            print('Обнаруженно деление на ноль')
            p2 = float(input("Введите делитель: "))
    s = p1 / p2

    return s


a = float(input("Введите делимое: "))
b = float(input("Введите делитель: "))
print('Результат ''%.2f' % fraction(a, b))
