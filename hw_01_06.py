a = float(input('a = '))
b = float(input('b = '))
d = 0
while a <= b:
    d = d + 1
    a = a + (a * 0.1)
print('Колличество дней', d)
