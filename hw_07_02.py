class Clothes:
    def __init__(self, title, V, H):
        self.title = title
        self.V = V
        self.H = H


    def res_coat(self):
        return f'{(self.V / 6.5 + 0.5):.2f}'


    def res_suit(self):
        return f'{(2 * self.H + 0.3):.2f}'


class Coat(Clothes):
    def __init__(self, title, V, H):
        Clothes.__init__(self, title, V, H)


class Suit(Clothes):
    def __init__(self, title, V, H):
        Clothes.__init__(self, title, V, H)


c = Coat('HM', 10, 10)
print(f'Ткани нужно на пальто {c.res_coat()}')
s = Suit('UNIQLO', 20, 15)
print(f'Ткани нужно на костюм {c.res_suit()}')