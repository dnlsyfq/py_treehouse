name = input("Please enter your name: ")

number = int(input("Please enter a number: "))




  

# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.
print(f"Hey {name}!")
print(f"The number is {number}...")

# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************
if (number % 5 == 0) and (number % 3 == 0):
  is_fizz = True
  is_buzz = True
  print("is a FizzBuzz number.")
elif number % 3 == 0 :
  is_fizz = True
  is_buzz = False
  print("is a Fizz number.")
elif number % 5 == 0:
  is_fizz = False
  is_buzz = True
  print("is a Buzz number.")
else:
  is_fizz = False
  is_buzz = False
  print("is neither a fizzy or a buzzy number.")

# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.


# Using the variables, check the condition of the value, and print the necessary
# string




















