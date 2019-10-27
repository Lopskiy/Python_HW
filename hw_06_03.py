class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        print(f'Имя сотрудника: {self.name}\nФамилия сотрудника: {self.surname}\nДолжность сотрудника: {self.position}')

    def get_full_profit(self):
        print(f'Доход сотрдника с учетом премии составляет: {sum(self._income.values())}')


a = Position('Иван', 'Иванович', 'Техник', {'profit': 10000, 'bonus': 5000})
a.get_full_name()
a.get_full_profit()
