def weekly_pay(): # keyword def with function name then ():
    """Prompts the user for name, hours worked and pay rate.  Returns name and earning in a week """  # docstring
    name = input("Please enter your name:")  # user input string
    try:
        hours_worked = int(input("Please enter how may hours you worked:"))  # user input int, possible ValueError
    except ValueError as err:
        raise ValueError
    try:
        hourly_pay_rate = float(input("Please enter your pay rate:"))
    except ValueError as err:
        raise ValueError
    else:
        return name + " " + "earned" + " " + "$" + str(hours_worked*hourly_pay_rate) + " " + "this week"

   # print(name, "worked", hours_worked, "hours", "at hourly rate of", hourly_pay_rate )  # print statement, minial formatting

if __name__ == '__main__':
    try:  # check for ValueError
        display_string = weekly_pay()  # function call
    except ValueError as err:
        print("ValueError encountered! ")
    else:
        print(display_string)
