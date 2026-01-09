from enum import nonmember
from typing import List

# break sample
# n=1
# while n<=10:
#     print(n)
#     n=n+1
#     if n>5:
#         print("Break")
#         break

# continue sample
# n=1
# while n<=10:
#     n=n+1
#     if n%2==0:
#         print("Continue")
#         # continue means skip the rest of the loop
#         continue
#     print(n)

# find the largest number
# for loop
# my_list=[1,2,3,4,6,5,7,8,9,10]
# largest = my_list[0]
# for i in my_list:
#     if i>largest:
#         largest = i
# print(largest)
# print("Done")

# find the largest number
# while loop
# my_list=[1,2,3,4,6,5,7,8,9,10]
# largest = my_list[0]
# i=0
# while i<len(my_list):
#     if my_list[i]>largest:
#         largest = my_list[i]
#     i=i+1
# print(largest)
# print("Done")


# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        else:
            inputNum=int(num)
    except ValueError:
        print("Invalid input")
        continue
    if largest is None and smallest is None:
        largest = inputNum
        smallest = inputNum
    elif inputNum>=largest:
        largest = inputNum
    elif inputNum<smallest:
        smallest = inputNum
print("Maximum is", largest)
print("Minimum is", smallest)

