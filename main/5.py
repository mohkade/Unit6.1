def multiply_string(n):
    n = n + 1
    return n

if __name__ == '__main__':
    try:
        n = int(input("Enter the number"))
    except ValueError as err:
        print("ValueError found!!")
    else:
        print("Python!" * n)
#    age = 5
 #   print(multiply_string(age))
  #  print(age)