# x = 'From marquard@uct.ac.za'

# find q and print out
# print(x[x.find("q")])

# slicing [ : ] print out uct
# portion_sliced="uct"
# length=len(portion_sliced)
# start=x.find(portion_sliced)
# print(x[start:start+length])
# second way but two times using the find function and bad readability, don't suggest
# portion_sliced="uct"
# print(x[x.find(portion_sliced):x.find(portion_sliced)+len(portion_sliced)])

# Uppercase method
# greet="Hello bob"
# print(greet.upper())

# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
number_start=text.find("0")
number_end=len(text)
number_extract=float(text[number_start:number_end])
print(number_extract)