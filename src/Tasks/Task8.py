"""
(Q)Triangle Classifier:
>Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.

"""

a = float(input("Enter the first side of triangle: \n"))
b = float(input("Enter the second side of triangle: \n"))
c= float(input("Enter the third side of triangle: \n"))

if a == b and a == c and b == c:
    print("Triangle is equilateral")
elif a == b != c or a == c != b or b == c != a:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")