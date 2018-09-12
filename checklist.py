import os

from termcolor import colored, cprint



checklist = []


def create(item):
    checklist.append(item)


def read(index):
    return checklist[index]


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for item in checklist:
        print("{} {}".format(index, item))
        index += 1


def un_mark(index):
    if '✓' in checklist[index]:
        uncheck = checklist[index]
        checklist[index] = uncheck[1:]

    else:
        text = colored('This item is not checked', 'red' , attrs = ['bold', 'blink'])
        print(text)

def mark_completed(index):

    checklist[index] = '✓' + checklist[index]
    print(checklist[index])


def select(function_code):
    # Create item
    if function_code.upper() == 'A':
        input_item = user_input("Input Item: ")
        create(input_item)

    # Check the item
    elif function_code.upper() == 'C':
        list_all_items()
        try:
            mark_completed(int(user_input("Please input the index number for desired item: ")))

        except TypeError:
            cprint("That was not a number.", 'red')

        except IndexError:
            cprint("That item does not exist", 'red')

    # Uncheck the item
    elif function_code.upper() == 'I':
        list_all_items()
        try:
            un_mark(int(user_input("Please input the index number for desired item: ")))

        except TypeError:
            cprint("That was not a number.", 'red')

        except IndexError:
            cprint("That item does not exist", 'red')

    # Read item
    elif function_code.upper() == "R":
        if not checklist:
            print("The list is empty")

        else:
            item_index = user_input("Index Number? ")
            try:
                print(read(int(item_index)))

            except IndexError:
                cprint("That item does not exist", 'red')

    # Print all items
    elif function_code.upper() == "P":
        list_all_items()

    # Delete a specific item
    elif function_code.upper() == "D":
        if not checklist:
            cprint("The list is empty", 'red')

        else:
            list_all_items()
            try:
                destroy(int(user_input("Input the index number to delete the desired item")))
            except IndexError:
                cprint("That item does not exist", 'red')
            except TypeError:
                cprint('That was not a number', 'red')

    # Quit the program
    elif function_code.upper() == "Q":
        exit()

    else:
        print('Unknown Option')


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def test():

    create('purple sox')
    create('red cloak')

    print(read(0))
    print(read(1))

    update(0, 'purple socks')
    destroy(1)

    print(read(0))

    # Call the new function "C"
    select("C")

    # View the result
    list_all_items()

    # Call the function with "R"
    select("R")

    # View the result
    list_all_items()

    # Call the function with "P"
    select("P")

    # View the result
    list_all_items()


# Run the code
textA = colored("A", 'yellow', attrs=['bold'])
textD = colored("D", 'magenta', attrs=['bold'])
textC = colored("C", 'green', attrs=['bold'])
textI = colored("I", 'red', attrs=['bold', 'dark'])
textR = colored("R", 'yellow', attrs=['bold'])
textP = colored("P", 'green', attrs=['bold', 'underline'])
textQ = colored("Q", 'red', attrs=['bold', 'underline', 'blink'])

while True:
    selection = user_input(
        "Press: " + textA + " to add to list\t " + textD + " to delete certain item\t" +
        textC + " to mark a certain items\t" + textI + " to un-mark a certain item\t" +
        textR + " to read list\t" + textP + " to display list\t" + textQ + " to quit")
    select(selection)

    if selection.upper() == "P":
        continue
    elif selection.upper() == "R":
        continue
    else:
        os.system('clear')
