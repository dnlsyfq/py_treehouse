### Side Note
Murphy's Law : anything that can go wrong will go wrong 


### user


input('')

### Python Basic

```
print(var,"")
```

* round()
* int()
* float()
* n // n # integer division
* n %  n # remainder

* print(" \n ")
* """  """
* len()
* var.upper()
* var.lower()
* var.title()
* str(var)
* print(f' {variable}')
* " {} {}".format(variableOne,variableTwo)
* "var" in "variable"

if condition:
    statement
elif condition:
    statement
else:
    statement

### Comparison

* isinstance(5,int)
* type(5) == int

### function

def name(param):
    statement

### try and except 

```
import math

def split_check(total, number_of_people):
    return math.ceil(total/number_of_people)

try:
    total_due = float(input("What is the total? "))
    number_of_people = int(input("How many people? "))
except ValueError:
    # not int and float
    print("Oh no! That's not a valid value. Try again...")
else:
    amount_due = split_check(total_due, number_of_people)
    print("Each person owes ${}".format(amount_due))
```

### try except raise 

```

import math


def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total/number_of_people)
try:

    total_due = float(input("What is the total? "))
    number_of_people = int(input("How many people? "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh no! That's not a valid value. Try again...")
    print("{}".format(err))
else:
    print("Each person owes ${}".format(amount_due))

```

### while loop 

```
import sys


password = input("Please enter the super secret password: ")
attempt_count = 1
while password != 'opensesame':
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to secret town")
```
### List

* len(list)
* list(string)
  
list method
* list.append(value)
* list.extend(list)
* list + list
* list.insert(index,value)
* del list
* del list[index]
* list.pop()
* list.pop(index)

* for i in list
* i in list
* list.copy()
* list.remove(variable)
* string.split(" ")
* ", ".join(list)

```
import time 
time.sleep(.5)
```
```
expenses = [
    [5,2.75,22,0,0],
    [24.75,5.50,15,22,8],
    [2.75,5.5,0,29,5]
]

week = 1
for i in expenses:
    print("Week {}: {}".format(week, sum(i)))
```
### Dictionary

dict = {
    key:value
}

* dict.keys()
* dict.values()
* sorted(dict.keys())
* del dict[key]

* for k,v in dict.items():
    print(k,v)

```
def print_teacher(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_teacher(name='Ashley', job='Instructor', topic='Python')
```

### loops 

* for i in variable:
    print(i)
  
* for index,element in enumerate(list):
    print(index,element)
  
* range(start,stop,step)

### sequence

* list[start:stop]
* list[::-1]
* 'character' in string
* 'character' not in string 
* string.count(value)
* string.index(value)
* list.index(value)
* list.reverse()

### function

```
def packer(*args):
    print(args)

packer('hi','i','love','python')
```

unpacking
```
def unpacker():
    return (1,2,3)

var1,var2,var3 = unpacker()
```

### dunder

* app.py
```
def print_hello():
  print("Hello from app")
  

if __name__ == '__main__':  
  print_hello()
```

* second_app.py
```
import app

print("Hello from second app")
app.print_hello()
```

### OOP 

dir(oop)

```
class Car:
    pass

class Car():
    pass

my_car = Car()

print(my_car)
print(type(my_car))
print(isinstance(my_car,Car))
```

* class attributes

```class Car:
    wheels = 4
    doors = 2
    engine = True

car_one = Car()
car_two = Car()

print(car_one.doors)
print(car_two.doors)
print(Car.doors)
```

* instance attributes 

```
class Car:
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
```

with default value
```
class Car:
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, model, year, make="Ford"):
        self.make = make
        self.model = model
        self.year = year
```

with method 
```
class Car:
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def stop(self):
        print('The car has stopped')

    def go(self,speed):
        print(f'The car going {speed}')


car_one = Car("Ford","Model T",1908)
car_one.stop()
car_one.go('slow')
```

with method 2
```
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
```

```
class Panda:
    species = 'Ailuropoda melanoleuca'
    food = 'bamboo'

    def __init__(self, name, age):
        self.is_hungry = True
        self.name = name
        self.age = age
        
    def eat(self):
        self.is_hungry = False
        return f'{self.name} eats {self.food}.'
```

* dunder string 

```
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
        
car_one = Car("Ford","Model T",1908)
print(str(car_one))        
```

* dunder iter 

```
class Dealership:

    def __init__(self):
        self.cars = ['Ford','Mazda','Honda']

    def __iter__(self):
        yield from self.cars

my_dealership = Dealership()
for car in my_dealership:
    print(car)
```

```
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
```

* dunder equal

```
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
```
```
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def __str__(self):
        return f'{self.author}, {self.title}'
    
    def __eq__(self, other):
        if self.author == other.author and self.title == other.title:
            return True
        else:
            return False
```

* separate class file

book.py
```
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def __str__(self):
        return f'{self.author}, {self.title}'
    
    def __eq__(self, other):
        if self.author == other.author and self.title == other.title:
            return True
        else:
            return False
```

bookcase.py
```
from book import Book


class BookCase:
    def __init__(self):
       self.books = []
    
    def __iter__(self):
        yield from self.books

    def add_books(self, book):
        self.books.append(book)
```