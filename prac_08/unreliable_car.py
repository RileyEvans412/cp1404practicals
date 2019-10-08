"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name="", fuel=0, reliability=69.69):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)

    def drive(self, distance=0):
        valid_drive = random.randint(0, 100)
        if valid_drive > self.reliability:
            drive = super().drive(distance)
            print("You drove {} kilometres".format(drive))
        else:
            print("Car broken down, you drove 0 metres")
