class Car:
    # pass
    wheels = 4
    doors = 2
    engine = True

    def __init__(self,  model, year, make="Ford"):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False

    def stop(self):
        if self.is_moving:
            print('The car has stopped')
            self.is_moving = False
        else:
            print('The car has already stopped')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car starts moving')
                self.is_moving = True
            print(f'The car is going {speed}')
        else:
            print('You have run out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True

    def __str__(self):
        '''Print Class Info'''
        return f'{self.make} {self.model} {self.year}'

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model



car_one = Car("Model T", 1908)
car_two = Car("Phantom", 2020, "Rolls Royce")

if car_one == car_two:
    print("equal")
else:
    print("not equal")

print(car_one)

print(car_one.make)
print(car_two.make)
print(car_one.year)
print(car_two.year)
print(car_one.doors)
print(car_two.doors)

car_one.stop()
car_one.go('fast')

print(Car.doors)
print(isinstance(car_one, Car))

car_one.doors = 4
Car.doors = 4
car_one.year = 2015

# __iter__
class Dealership:
    # cars = ['Ford Fusion','Honda Civic','Dodge Dakota']

    def __int__(self):
        self.cars = []

    def __iter__(self):
        yield from self.cars

    def add_car(self,car):
        self.cars.append(car)


my_dealership = Dealership()
my_dealership.add_car('bmw')
for car in my_dealership:
    print(car)

