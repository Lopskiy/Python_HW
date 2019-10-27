from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print(self.__color[0])
        sleep(7)
        print(self.__color[1])
        sleep(2)
        print(self.__color[2])


a = TrafficLight()
a.running()
