# def minimum(first, second):
#     if (first < second):
#         return first
#     return second
from src.August.ex_13082024.Lab016 import name2


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called")
#         func()
#         print("Something is happening after the function is called")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello World")
#
# say_hello()

# import time
#
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
#         return result
#     return wrapper
#
# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("Function finished")
#
# slow_function()

# class MyClass:
#     @staticmethod
#     def static_method():
#         print("This is a static Method")
# MyClass.static_method()

# class MyClass:
#     class_variable = "Hello"
#     @classmethod
#     def class_method(cls):
#         print(f"Class_Variable value:{cls.class_variable}")
# MyClass.class_method()

# class MyClass:
#     def __init__(self,value):
#         self.value = value
#
#         @property
#         def value(self):
#             return self.value
#
#         @value.setter
#         def value(self, new_value):
#             self.value = new_value
#
# obj = MyClass(10)
# print(obj.value)
# obj.value = 20
# print(obj.value)

# import functools
#
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Before the function calls")
#         result = func(*args, **kwargs)
#         print("After the function is called")
#         return result
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()

# class MyClass:
#
#     @staticmethod
#     def static_method(self):
#         print("This is static method")
#
#     @classmethod
#     def class_method(cls):
#         print(f"This is class method of {cls}")
#
#     @property
#     def name(self):
#         return "MyClass"
#
# obj = MyClass()
# obj.static_method()
# obj.class_method()
# print(obj.name)

# def decorator1(func):
#     def wrapper():
#         print("Decorator 1")
#         func()
#     return wrapper
#
# def decorator2(func):
#     def wrapper():
#         print("Decorator 2")
#         func()
#     return wrapper()
#
# @decorator1
# @decorator2
# def say_hello():
#     print("Hello!")
#
# say_hello()

# import functools
#
# def log_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args} and {kwargs}")
#         result = func(*args, **kwargs)
#         print(result)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper
#
# @log_decorator
# def add(a,b):
#     return a + b
#
# add(2, 3)

triple = lambda num: num * 3
print(triple(10))