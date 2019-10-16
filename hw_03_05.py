def sum_f(a):
    global theSum, exit_f
    for i in a:
        theSum = theSum + i
        if i == 0:
            exit_f = 1
            return exit_f
    return theSum


exit_f = 0
theSum = 0
s = 0
answer = ''
while exit_f != 1:
    sum_f([float(i) for i in input('Введите числа через пробел (Для выхода введите 0) : ').split()])
    print('Сумма чисел:','%.2f' %  theSum)
