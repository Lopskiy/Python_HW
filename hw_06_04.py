class Car_class:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала ')

    def stop(self):
        print(f'Машина {self.name} остановилась ')

    def turn(self, direction):
        print(f'Машина {self.name} поавернула {direction} ')


class TownCar(Car_class):
    def __init__(self, speed, color, name, is_police):
        Car_class.__init__(self, speed, color, name, is_police)


class SportCar(Car_class):
    def __init__(self, speed, color, name, is_police):
        Car_class.__init__(self, speed, color, name, is_police)


class WorkCar(Car_class):
    def __init__(self, speed, color, name, is_police):
        Car_class.__init__(self, speed, color, name, is_police)


class PoliceCar(Car_class):
    def __init__(self, speed, color, name, is_police):
        Car_class.__init__(self, speed, color, name, is_police)


car1 = TownCar(100, 'Белая', 'Lexus', False)
car1.go()
car1.turn('Направо')
car1.stop()

car2 = SportCar(200, 'Красная', 'Ferrari', False)
car2.go()
car2.turn('Налево')
car2.stop()

car3 = WorkCar(70, 'Серый', 'ГАЗ', False)
car3.go()
car3.turn('Направо')
car3.stop()

car4 = PoliceCar(80, 'Черный', 'Hundai', True)
car4.go()
car4.turn('Налево')
car4.stop()
