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
