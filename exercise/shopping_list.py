
shopping_list = []

def show_help():
    print("""
        Enter DONE to exit
        Enter HELP to get help
        Enter SHOW to get list
    """)


def add_to_list(item):
    shopping_list.append(item)


def show_list():
    print("Shopping List: \n")
    for i in shopping_list:
        print("* " + i)


print("Enter DONE/HELP/SHOW")


while True:
    new_item = input("> ")

    if new_item == 'DONE':
        print("System Quit")
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)


show_list()