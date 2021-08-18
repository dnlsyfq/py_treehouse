# def yell(text):
#     text = text.upper()
#     number_of_characters = len(text)
#     result = text + "!" * (number_of_characters // 2)
#     print(result)
#
#
# yell("You are doing great")

# import math
#
# def split_check(total, number_of_people):
#     return math.ceil(total/number_of_people)
#
# try:
#     total_due = float(input("What is the total? "))
#     number_of_people = int(input("How many people? "))
# except ValueError:
#     # not int and float
#     print("Oh no! That's not a valid value. Try again...")
# else:
#     amount_due = split_check(total_due, number_of_people)
#     print("Each person owes ${}".format(amount_due))

#
# import math
#
#
# def split_check(total, number_of_people):
#     if number_of_people <= 1:
#         raise ValueError("More than 1 person is required to split the check")
#     return math.ceil(total/number_of_people)
# try:
#
#     total_due = float(input("What is the total? "))
#     number_of_people = int(input("How many people? "))
#     amount_due = split_check(total_due, number_of_people)
# except ValueError as err:
#     print("Oh no! That's not a valid value. Try again...")
#     print("{}".format(err))
# else:
#     print("Each person owes ${}".format(amount_due))
#
#

# import sys
#
#
# password = input("Please enter the super secret password: ")
# attempt_count = 1
# while password != 'opensesame':
#     if attempt_count > 3:
#         sys.exit("Too many invalid password attempts")
#     password = input("Invalid password, try again: ")
#     attempt_count += 1
# print("Welcome to secret town")

# expenses = [
#     [5,2.75,22,0,0],
#     [24.75,5.50,15,22,8],
#     [2.75,5.5,0,29,5]
# ]
#
# week = 1
# for i in expenses:
#     print("Week {}: {}".format(week, sum(i)))


### OOP

class Car:

    wheels = 4
    doors = 2
    engine = True



    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_moving = False
        self.gas = 100

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def __eq__(self,other):
        return self.make == other.make and self.model == other.model


    def stop(self):
        if self.is_moving:
            print('The car has stopped')
            self.is_moving = False
        else:
            print('The car already stopped ')

    def go(self,speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car starts moving')
                self.is_moving = True
            print(f'The car going {speed}')
        else:
            print('You have run out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True

class Dealership:

    def __init__(self):
        self.cars = []

    def __iter__(self):
        yield from self.cars

    def add_car(self,car):
        self.cars.append(car)



car_one = Car("Ford","Model T",1908)
car_two = Car('Mazda','3',2020)

my_dealership = Dealership()
my_dealership.add_car(car_one)
my_dealership.add_car(car_two)
for car in my_dealership:
    print(car)

# print(str(car_one))

# car_two = Car("Rolls Royce","Phantom",2020)


# print(car_one.doors)
# print(car_two.doors)
# print(Car.doors)
#
#
# car_one.doors = 4
# print(car_one.doors)

# print(car_one.make)
# print(car_two.make)