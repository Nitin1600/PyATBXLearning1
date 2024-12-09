# Create a program to sum of three number from the user input

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

def sum_of_three_numbers(num1,num2,num3):
    return num1 + num2 + num3

result = sum_of_three_numbers(num1,num2,num3)
print(result)