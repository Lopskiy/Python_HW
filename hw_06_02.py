class Road:
    def __init__(self, _width, _length):
        self._width = _width
        self._length = _length

    def road_mass(self):
        asp_mass = float(input('Введите массу асфальта: '))
        thickness = float(input('Введите толщину дороги см: '))
        full_mass = (self._length * self._width * asp_mass * thickness) / 1000
        print(f'Масса всей дороги {full_mass} т')


a = float(input('Введите длину: '))
b = float(input('Введите ширину: '))
road_ = Road(a, b)
road_.road_mass()
