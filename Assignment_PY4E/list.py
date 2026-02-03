# range function as index during iteration
# list_01 = [2, 'red', [5, 6.01]]
# print("""list before iteration: """+str(list_01))
# for i in range(len(list_01)):
#     print(i)
#     if i+1 < len(list_01):
#         temp = list_01[i]
#         list_01[i] = list_01[i + 1]
#         list_01[i + 1] = temp
#     print("list current status: "+str(list_01))
# print("list after iteration: "+str(list_01))

# 8.4 List assignment
#     Open the file romeo.txt and read it line by line.
#     For each line, split the line into a list of words using the split() method.
#     The program should build a list of words. For each word on each line check to see
#     if the word is already in the list and if not append it to the list.
#     When the program completes, sort and print the resulting words in python sort()
#     order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     words=line.split()
#     for word in words:
#         if word not in lst:
#             lst.append(word)
# lst.sort()
# print(lst)

# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
#
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    words=line.split()
    if len(words)<=2:
        continue
    count = count+1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")










