def multiply_string():
    name = input("Please enter your name:")  # user input string
    try:
        n = int(input("Please enter how many times you would like your name to show up:"))  # user input int, possible ValueError
    except ValueError as err:
        raise ValueError  # Seems silly, but later we can define custom exceptions!
    else:
        return str(name*n)  # return statement, string concatenation

if __name__ == '__main__':
    try:  # check for ValueError
        display_string = multiply_string()  # function call
    except ValueError as err:
        print("ValueError encountered! ")
    else:
        print(display_string)






if __name__ == '__main__':
    pass
