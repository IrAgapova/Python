import random


class Car:
    direction = ["north", "east", "south", "west"]
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police= is_police
        print(f'Машина:{name} цвет: {color}.\n Полицейская машина? {is_police}')

    def go(self):
        print(f'{self.name}:Машина поехала')

    def stop(self):
        print(f'{self.name}:Машина остановилась')

    def turn(self):
        print(f'{self.name}: Машина повернула{random.choice(self.direction)}')

    def show_speed(self):
        return f"{self.name}:Скорость машины: {self.speed}"
class TownCar(Car):

    def show_speed(self):
        return f"{self.name}: Скорость:{self.speed}. Осторожно!" if self.speed > 60 else super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}: Скорость:{self.speed}. Осторожно!" if self.speed > 40 else super().show_speed()

class SportCar(Car):
    """ Спортивная машина"""

class PoliceCar(Car):
    def __init__(self, name, color, speed ):
        super().__init__(name, color, speed, is_police=True)

police_car= PoliceCar ("Форд", "белый", 90)
work_car= WorkCar("Камаз", "красный", 46)
sport_car= SportCar("Феррари", "желтая", 100)
town_car = TownCar ("Киа", "синяя", 65)

list_of_cars = [police_car, work_car, town_car, sport_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()



