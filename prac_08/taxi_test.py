"""
CP1404/CP5632 Practical
Car class Test
"""
from prac_08.taxi import Taxi

taxi_1 = Taxi("Prius 1", 100)

taxi_1.start_fare()
taxi_1.drive(40)
print("{}, {}".format(taxi_1.__str__(), taxi_1.get_fare()))
taxi_1.start_fare()
taxi_1.drive(100)
print("{}, {}".format(taxi_1.__str__(), taxi_1.get_fare()))



