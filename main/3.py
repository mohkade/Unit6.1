def get_user_input(): # keyword def with function name then ():
    """Prompts the user for name, age and prints a message"""  # docstring
    name = input("Please enter your name:")  # user input string
    try:
        age = int(input("Please enter your age:"))  # user input int, possible ValueError
    except ValueError as err:
        raise ValueError  # Seems silly, but later we can define custom exceptions!
    else:
        return name + " " + str(age) + " years old. "  # return statement, string concatenation


if __name__ == '__main__':
    try:  # check for ValueError
        display_string = get_user_input()  # function call, store in a variable
    except ValueError as err:
        print("ValueError encountered! ")
    else:
        print(display_string)  # print the result of the function