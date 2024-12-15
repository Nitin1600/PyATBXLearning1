try:
    num1 = int(input("enter the num1: \n"))
    num2 = int(input("enter the num2: \n"))
    result = num1/num2
except ValueError as ve:
    print("Value Error, you have entered string, instead we want integer")
except ZeroDivisionError as zde:
    print("DOn't try to divide by zero")
else:
    print(f"The result is {result}")
finally:
    print("This code will always be executed")