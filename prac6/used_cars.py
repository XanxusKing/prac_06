from prac6.car import Car


def main():
    """Demo test code to show how to use car class."""
    #my_car = Car(180)
    #my_car.drive(30)
    limo=Car(100,"my limousine")
    limo.add_fuel(20)

    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)

    print("Car {}, {}".format(limo.fuel, limo.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=limo))


main()