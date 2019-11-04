class Complex:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        return self.x / other.x


a = Complex(2j)
b = Complex(3j)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
