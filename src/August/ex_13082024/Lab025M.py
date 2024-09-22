# x = input("Type a number: ")
# y = input("Type another number: ")
# sum = int(x) + int(y)
# print("The Sum is ", sum)

# print(complex(2.5, -18.2))
# c = complex(2.5, -18.2)
# c = c + 1
# print(c)

# print(r'C:\some\name')

# random_string = "I am a Batman"
# print(len(random_string))

# batman = "Bruce Wayne"
# first = batman[0]
# print(first)
# space = batman[5]
# print(space)
# last = batman[len(batman) - 1]
# print(last)
# # err = batman[len(batman)]
# # print(err)
# print(batman[-1])
# print(batman[-5])

# string = "I am immutable"
# string[0] = '0'

# str1 = "Amit"
# print(id(str1))
# str1 = "Wadyar"
# print(id(str1))

# val = None
# print(val)
# print(type(val))

# my_string = "I am learning Python"
# print(my_string[0:4])
# print(my_string[1:7])
# print(my_string[8:len(my_string)])

# my_string = "This is Amit from Bengaluru"
# print(my_string[0:7])
# print(my_string[0:7:2])
# print(my_string[0:7:5])

# my_string ="This is Amit!@"
# print(my_string[13:2:-1])
# print(my_string[17:0:-2])
#
# my_string = "This is MY string"
# print(my_string[:8])
# print(my_string[8:])
# print(my_string[:])
# print(my_string[::-1])
#
# txt = "Hello World"[::-1]
# print(txt)

# String1 = "Hello, I'm a Pramod"
# list1 = list(String1)
# print(list1)
# list1[2] = 'p'
# String2 = ''.join(list1)
# print(String2)

# String1 = "Hello, Pramod"
# print("Initial String: ")
# print(String1)
#
# String2 = String1[0:2] + String1[3:]
# print("\nDeleting character at 2nd Index")
# print(String2)
#
# del String1
# print(String1)

# print("\nEscaping Backslashes: ")
# print("This is a backslash \\")
# print("This is the new line \nThis is the second line")
# print("This is a tab\tThis is after the tab")

# print(r"This is a backslash \\")

# string1 = "I like %s" % "python"
# print(string1)
#
# temp = "TTA"
# string2 = "I like %s" % temp
# print(string2)
#
# string3 = "I like %s and %s" % ("python", temp)
# print(string3)
#
# my_string = "%i + %i = %i" % (1,2,3)
# print(my_string)

string1 = "%f" % (1.11)
print(string1)

string2 = "%.2f" % (1.11)
print(string2)

string3 = "%.2f" % (1.117)
print(string3)