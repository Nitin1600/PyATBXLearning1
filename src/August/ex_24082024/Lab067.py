#1.NRNA

# def greet():
#     print("Hello World")
#
# result = greet()
# print(result)

#NRWA:

# def greet_by_name(name):
#     print("Hello,", name)
#
# greet_by_name("Amith")

#NRWDA:

# def say_hello_default_arg(name="pramod"):
#     print("Hello,", name.upper())
#
# say_hello_default_arg("Amith")
# say_hello_default_arg()
# say_hello_default_arg(name="Ram")

# def multiple_args(name1="Akash", name2="Abahy", name3="Uday"):
#     print("Multiple Arguments", name1, name2, name3)
#
# multiple_args(name1="Zebra", name2="Horse", name3="Cat")
# multiple_args(name1="PRAMOD")
#
# def multiple_args(name1="Arpita", name2="Pramod", name3="Amit"):
#     print("Multiple Arguments", name1, name2, name3)
#
#
# multiple_args(name1="Ram", name2="Yunus", name3="Deepshikha")
# multiple_args(name1="Elephant")

#R+A:

def sum_of_two_numbers(num1, num2):
    return num1 + num2

def sum_of_two_numbers_with_default(num1=100, num2=200):
    return num1 + num2

result1 = sum_of_two_numbers(200, 300)
result2= sum_of_two_numbers_with_default()
print(result1)
print(result2)
