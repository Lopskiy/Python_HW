from math import factorial


def fibo_gen():
    generator = range(1, 15)
    for i in generator:
        yield factorial(i)


for el in fibo_gen():
    print(el)
