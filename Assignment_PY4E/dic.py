# practice 01
# If you have a dictionary called `fruit_counts` that contains the number of different fruits,
# how would you increment the count of 'apples' by 1?
# What would the code look like?
# fruit_counts = {'apples': 3, 'oranges': 5, 'pears': 2}
# if 'apples' in fruit_counts:
#     fruit_counts['apple'] += 1
# else:
#     fruit_counts['apple'] = 1
# print(fruit_counts)

# If you have a dictionary called employee_salaries
# that contains employee names as keys and their salaries as values,
# how would you calculate the total salary of all employees?
# What would the code look like?
# employee_salaries = {'Alice': 5000, 'Bob': 6000, 'Charlie': 4500}
# total_salary = sum(employee_salaries.values())/len(employee_salaries)

# Exercise 9.4
# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines
# as the person who sent the mail.
# The program creates a Python dictionary that maps(映射) the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop
# to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
try:
    with open(name) as handle:
        # 1. looks for 'From ' lines
        counts = dict()
        for line in handle:
            if 'From ' in line:
                # 2. takes the second word of those lines
                words = line.split()
                counts[words[1]] = counts.get(words[1], 0) + 1
    # check if dictionary is empty
    if len(counts) < 1:
        raise ValueError("Dictionary is empty")
except FileNotFoundError:
    print("File not found")
# 3. using maximum loop to find the most prolific committer
largest = 0
email_largest = None
for email, count in counts.items():
    if count > largest:
        largest = count
        email_largest = email
print(email_largest, largest)
