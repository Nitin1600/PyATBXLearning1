# a = lambda a: a ** 2
# print(a(4))

# def square(x):
#     return x ** 2
#
# numbers = [1,2,3,4,5]
# squared_numbers = map(square, numbers)
#
# for result in squared_numbers:
#     print(result)

# def square(x):
#     return x ** 2
#
# numbers = [1,2,3,4,5]
# squared_numbers = map(square, numbers)
#
# result = list(squared_numbers)
# print(result)

# numbers = [1,2,3,4,5]
#
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))

# def is_even(x):
#     return x % 2 == 0
#
# numbers = [1,2,3,4,5]
# even_numbers = filter(is_even, numbers)
#
# result = list(even_numbers)
# print(result)

# numbers = [1,2,3,4,5]
#
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# result = list(even_numbers)
# print(result)

# numbers = [1,2,3,4,5]
#
# squared_numbers = map(lambda x: x ** 2, numbers)
# result = list(squared_numbers)
# print(result)

# def greet(name = "World"):
#     print("Hello, " + name + "!")
#
# greet()
# greet("Alice")

# def rec_count(number):
#     print(number)
#
#     if number == 0:
#         return 0
#     rec_count(number - 1)
#
# rec_count(5)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# result = fibonacci(6)
# print(result)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# result = factorial(5)
# print(result)

# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0] + sum_list(lst[1:])
#
# result = sum_list([1,2,3,4,5])
# print(result)

squares = [i**2 for i in range(10)]
print(squares)