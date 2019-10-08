"""
CP1404/CP5632 Practical
Unreliable Car class Test
"""
from prac_08.unreliable_car import UnreliableCar

car_1 = UnreliableCar("Shitbox", 200)
car_1.drive(100)
print("{}".format(car_1.__str__()))
