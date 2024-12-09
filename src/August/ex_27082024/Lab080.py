def add_extra_security(func):
    def wrapper():
        print("1.Before the function is called")
        print("2.Add 'helmet','dashcams','gear','gown'")
        func()
        print("3.After the function is called")
        print("4.Secure driving")
    return wrapper()

# @my_decorator
#     def my_bike():
#         print("I am driving")

@add_extra_security
def my_scooty():
    print("Normal function")

# ✅ Understanding Decorators in Python
#
def add_extra_security(func):
    # two parts
    # wrapper & call
    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcash, gloves, knee guards")
        # drive_bike()
        func()
        print("3.After the function is called.")
        print("4.Secure Driving")

    return wrapper()


# definition
# @my_decorator
# def drive_bike():
#     print("I am driving")

@add_extra_security
def drive_scooty():
    print("Normal Function")