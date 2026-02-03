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
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)









