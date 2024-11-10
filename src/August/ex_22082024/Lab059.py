# Match Statement
# Switch in Java
# match the op and execute
# Python > 3.10

# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block

# Write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser: \n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name == "firefox":
            print("Hello Hello!")
        print("Execute firefox code")
    case "chrome":
        print("Execute chrome code")
    case "edge":
        print("Execute edge code")
    case "safari":
        print("Execute safari code")
    case _:
        print("Browser not found!")