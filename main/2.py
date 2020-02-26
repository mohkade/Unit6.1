def get_user_input(): # keyword def with function name then ():
    """Prompts the user for name, age and prints a message"""  # docstring
    name = input("Please enter your name:")  # user input string
    try:
        age = int(input("Please enter your age:"))  # user input int, possible ValueError
    except ValueError as err:
        raise ValueError  # Seems silly, but later we can define custom exceptions!
    else:
        print(name, " ", age, " years old. ")  # print statement, minimal formatting


if __name__ == '__main__':
    try:  # check for ValueError
        get_user_input()  # function call
    except ValueError as err:
        print("ValueError encountered! ")