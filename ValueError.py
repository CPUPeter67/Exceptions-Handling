try:
    number = int(input("Enter a number: "))
    print("The number you have entered is", number)
except ValueError as ex:
    print("The exception is:", ex)
   