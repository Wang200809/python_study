#7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
import os.path

# Use words.txt as the file name
#
# file_name = input("Enter file name: ")
# file_path = os.path.join("doc", file_name)
# try:
#     with open(file_path) as file:
#         for line in file:
#             line = line.rstrip()
#             print(line.upper())
# except FileNotFoundError:
#     print("File not found")

# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# values=0
# count=0
# with open(fname) as fh:
#     for line in fh:
#         if not line.startswith("X-DSPAM-Confidence:"):
#             continue
#         # extract the floating point value
#         value=line[line.find(':')+1:]
#         values+=float(value)
#         count+=1
#         print(line)
#     print("Average spam confidence:",values/count)
#     print("Done")
#

# test
file=open("test.txt")
for line in file:
    # print(line)
    print(line.rstrip())