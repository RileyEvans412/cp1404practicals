"""
CP1404 Practical - Code for car class
"""

from prac_06.car import Car


def main():
    my_car = Car("My car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print('Limo {}'.format(limo.fuel))
    limo.drive(115)
    print('Limo odo: {}'.format(limo.odometer))
    print('Limo {self.fuel}, {self.odometer}'.format(self=limo))


main()
