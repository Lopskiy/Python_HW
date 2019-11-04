class Stock:
    def __init__(self, units):
        self.units = units


class Office_equipment:
    def __init__(self, name, color, units):
        self.name = name
        self.color = color
        self.units = units


class Printer(Office_equipment):
    def __init__(self, name, color, print_speed, units):
        super().__init__(name, color, units)
        self.print_speed = print_speed
        print(name, color, print_speed, units)


class Scanner(Office_equipment):
    def __init__(self, name, color, scan_speed, units):
        super().__init__(name, color, units)
        self.scan_speed = scan_speed
        print(name, color, scan_speed, units)


class Xerox(Office_equipment):
    def __init__(self, name, color, recive_speed, units):
        super().__init__(name, color, units)
        self.recive_speed = recive_speed
        print(name, color, recive_speed, units)


p = Printer('HP', 'White', '10 p/m', 15)
s = Scanner('Samsung', 'Black', '7 p/m', 25)
x = Xerox('Benq', 'Grey', '22 p/m', 4)

