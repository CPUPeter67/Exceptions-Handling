try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1 / num2
    print("The result is", result)

except ZeroDivisionError:
    print("You cannot divide by zero. It is an error!")

except SyntaxError:
    print("A comma is missing (,). Please enter two numbers seperated by a comma like this: 1, 2")

except:
    print("This is the wrong input format.")

else:
    print("There are no exceptions.")

finally:
    print("This will execute no matter what.")