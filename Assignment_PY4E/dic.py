#practice 01
# If you have a dictionary called `fruit_counts` that contains the number of different fruits,
# how would you increment the count of 'apples' by 1?
# What would the code look like?
# fruit_counts = {'apples': 3, 'oranges': 5, 'pears': 2}
# if 'apples' in fruit_counts:
#     fruit_counts['apple'] += 1
# else:
#     fruit_counts['apple'] = 1
# print(fruit_counts)

#If you have a dictionary called employee_salaries
# that contains employee names as keys and their salaries as values,
# how would you calculate the total salary of all employees?
# What would the code look like?
employee_salaries = {'Alice': 5000, 'Bob': 6000, 'Charlie': 4500}
total_salary = sum(employee_salaries.values())/len(employee_salaries)