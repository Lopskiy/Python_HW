def my_func(v_1, v_2, v_3):
    if v_1 < v_2:
        min_f = v_1
    else:
        min_f = v_2
        if v_3 < min_f:
            min_f = v_3

    s = v_1 + v_2 + v_3 - min_f
    print('Сумма наибольших двух аргументов', '%.2f' % s)


my_func(float(input('Введите первое число ')), float(input('Введите второе число ')),
        float(input('Введите третье число ')))
