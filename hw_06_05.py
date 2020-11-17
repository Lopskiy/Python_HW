class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Рисунок ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисунок карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисунок маркером {self.title}')


picture1 = Stationery('Имя')
picture1.draw()
picture2 = Pen('Имя')
picture2.draw()
picture3 = Pencil('Имя')
picture3.draw()
picture4 = Handle('Имя')
picture4.draw()
