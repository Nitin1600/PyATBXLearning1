score = int(input("Enter your score\n"))
if 90 <= score <= 100:
    print("Your grade is ", "A")
elif 80 <= score <= 89:
    print("Your score is ", "B")
elif 70 <= score <= 79:
    print("Your grade is ", "C")
elif 60 <= score <= 69:
    print("Your grade is ", "D")
elif score > 100:
    print("You are a superman!!")
else:
    print("Your grade is ", "F")