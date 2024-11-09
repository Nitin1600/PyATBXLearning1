# for i in range(5):
#     print(i)

# numbers = list(range(10))
# print(numbers)

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# count = 0
#
# while True:
#     count += 1
#     print(f"This will print atleast once. Count = {count}")
#
#     if count >= 5:
#         break
#
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# for num in range(2,10):
#     if num % 2 == 0:
#         print("Found an even num", num)
#         continue
#     print("Found an odd number", num)

parameter = "Pramoda"

match parameter:
    case "Pramod":
        print("Hi")
    case "PramOD":
        print("2")
    case "Pramoda":
        print("Hello")
    case _:
        print("Default")