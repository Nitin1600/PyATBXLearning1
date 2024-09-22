"""

Take two numbers and fetch

-Add,Div,Mul,Pow,Sub,Pow,Max.
-Format output in string format

"""

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

max_num = max(num1,num2)
print("Maximum number is: ", f"{max_num}")

Sum = num1+num2
print("Sum is: ", f"{Sum}")

Pow = num1**num2
print("Power is: ", f"{Pow}")

Sub = num1-num2
print("Sub is: ", f"{Sub}")

Mul = num1*num2
print("Mul is: ", f"{Mul}")

Div = num1/num2
print("Div is: ", f"{Div}")