### Side Note
Murphy's Law : anything that can go wrong will go wrong 


### user


input('') // produce string
```
# TODO: Prompt the user for parts of speech and store them in variables
verb = input("Enter verb: ")
noun = input("Enter noun: ")
adjective = input("Enter adjective: ")

# TODO: Output the template to the screen with the blanks filled out with what the user stated
print(f"I enjoy practice! I find it helps me to {verb} better.")
print(f"Without practice, my {noun} would probably not even work.")
print(f"My code is getting more {adjective} every single day!")
```

### Python Basic

```
// print command can take multiple values to output on the same line.
print(var,"")
print("Balance:", 5000)
print("Iron", "Man", sep ="-")

result = 798
currency = "$"
print("Total:", currency, result)
```

* round()
* int()
* float()
* n // n # integer division
* n %  n # remainder

* \ escape character
* print(" \n ")
* """  """
* len(var)
* var.upper()
* var.lower()
* var.title()
* str(var)
* print(f' {variable}')
* " {} {}".format(variableOne,variableTwo)
* "var" in "variable"
* bool(0) // False
* bool(1) // True
* bool("") // False
* bool("word") // True
* not True
* not False
* True and True

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

```
i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")
```

```
i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)
```

### Tuples
* immutable
```
Tuples vs. Lists
Reassignment and Immutability
Use lists when you need to change your data or append more items.

Because tuples are immutable, they can't be altered. That means they aren't the right choice when you need to loop over data and append it to a data structure.

Variable size
Use tuples when your data is fixed and pre-determined.

Lists are variable in size, meaning you can always add or remove items from them. That's why lists are the right choice when you don't know their contents ahead of time.

Tuples can't be added to, so you need to know their contents ahead of time. They are a good choice if you have a fixed set of data.

Homogeneous vs Heterogeneous Content
Use tuples for heterogeneous data and lists for homogeneous data

Tuples are often used to store heterogeneous data. This meaning, if you have a mix of types, you'd probably use a tuple. Lists, however, are mostly used when you have homogeneous data - when all your data is of the same type.

This is a semantic difference, and is not something that would impact the functionality of your code. It is a common use case, though. That's because lists are commonly used when you want to loop over data and perform an action on each item. That's easy to do without error if all items in a list are of the same type.

Tuples, on the other hand, are fixed and created with pre-determined data. This means tuples can follow a "schema" that describes something. See the following example

# A tuple might contain data about a person (heterogeneous type mixture)
person_a = (name, age, occupation, address)

# A list might contain a list of people (homogeneous type mixture - all tuples!)
people = [person_a, person_b, person_c]
Efficiency
Use tuples for faster and more efficient access.

Because tuples are immutable, they are accessed more quickly and are more memory efficient than lists. This means that, as long as you know your data isn't going to change, a tuple is the more performant choice.
```

```
groceries = 'apples', 'oranges', 'lettuce', 'cheddar cheese'
groceries = ('apples', 'oranges', 'lettuce', 'cheddar cheese')

# A tuple!
my_tuple = 1,

# The same tuple!
my_tuple = (1,)
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


### Function packing and unpacking
```

def packer(*args):
    print(args)

packer('hi','i','love','you')


def packer(*args):
    for val in args:
        print(val)
        
packer('hi','i','love','you')    


def calculate_total(*args):
    total = sum(args)
    print(total)

calculate_total(24,23,12)

def print_teacher(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_teacher(name='Ashley', job='Instructor', topic='Python')
```

### Function unpacking
```
def unpacker():
    return (1,2,3) // work with list
    
var1 ,var2 , var3 = unpacker()   

first, last = input('Enter full name: \n').split(' ')
```

### loops 
```
for i in variable:
   print(i)
  
for index,element in enumerate(list):
   print(index,element)
   
for index,element in enumerate(list,1):
   print(index,element)   
   
index = 1
for item in groceries:
    print(f'{index}. {item}')
    index += 1
  
* range(start,stop,step)
```
### sequence

* list[start:stop:step]
* list[::-1] // all but reverse order
* 'character' in string
* 'character' not in string 
* string.count(value)
* string.index(value)
* list.index(value)
* list.reverse()

// work with tuples, string
* len(list)
* max(list)
* min(list)

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
