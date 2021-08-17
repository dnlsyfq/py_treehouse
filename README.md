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


