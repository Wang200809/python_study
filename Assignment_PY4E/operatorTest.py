# This first line is provided for you
# Pay calculator
# hrs = input("Enter Hours: ")
# rate=input("Enter Rate: ")
# print("Pay: "+str(float(hrs)*float(rate)))

# if  statement
# age=int(input("Enter age: "))
# if age>=18:
#     print("Adult")
# elif age>=13:
#     print("Teenager")
# else:
#     print("Child")

# if  statement & try except
age=None
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Pls enter integer number as age")
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
elif age <= 0:
    print("Pls enter age larger than 0")
else:
    print("Child")


# 3.3 Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.
# For the test, enter a score of 0.85.
# try:
#     score = float(input("Enter Score: "))
#     if score>=1.0 or score<0.0:
#         print("Pls enter a number between 0.0 and 1.0")
#     elif score>=0.9:
#         print("A")
#     elif score>=0.8:
#         print("B")
#     elif score>=0.7:
#         print("C")
#     elif score>=0.6:
#         print("D")
#     else:
#         print("F")
# except ValueError:
#     print("Pls enter a number")

