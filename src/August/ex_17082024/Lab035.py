# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)

# Logic Building Formula

# Step 1 Figure out the inputs and output
# input -> r -> data type -> float
# pi -> 3.14 , math.pi
# power -> pow or ** -> any

# o/p -> float - area , print area

# Step 2
# rough logic =  area = 3.14 * pow(r,2)

# Step 3 - Write the logic

import math

radius = float(input("Enter the radius of the circle\n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius,2)
area2 = 3.14 * (radius**2)
print("Area of the circle -> ", area)
print("Area of the circle -> ", area2)
print(f"Area of the circle -> {area:.2f}")

print(3.1415*(float(input("Enter the radius of the circle\n"))**2))