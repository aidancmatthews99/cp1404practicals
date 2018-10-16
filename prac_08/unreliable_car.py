from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name='', fuel=0, reliability=randint(0, 100)):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        elif self.reliability < randint(0, 100):
            self.fuel -= distance
            print('Trip failed')
        else:
            distance = 0
        self.odometer += distance
        return distance