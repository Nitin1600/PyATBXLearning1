print("------Start of the Programme------")

try:
    a = int(input("Ent the num1")) # ValueError: invalid literal for int()
    b = int(input("Ent the num2"))
    c = a / b # ZeroDivisionError: division by zero - Lab149.py", line 3
    print("Result Div is ", c)
except Exception as e:
    print(e)
    print("Please check your inputs, it shouldn't be a string or zero")

print("------End of the Programme------")