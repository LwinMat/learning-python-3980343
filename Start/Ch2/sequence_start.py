# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
print("Lists")
mylist = [0, 1, "two", 3.2, False]

print(len(mylist))

# to access a member of a sequence type, use []
# access to the element in index 2
print("\nAccess to Members")
print(mylist[2]) 

# get the last element in the list
print(mylist[-1])

# change value in an specific index
mylist[0] = 10

print(mylist)


# add a list to another list
print("\nAdding list to another list")
another_list = [6,7,10]
mylist = mylist + another_list
print(mylist)

mystr = "This is a string"
print(mystr[2])
# mystr[2] = "Z" -> causes an error

# use slices to get parts of a sequence
print("\nSlicing")
print(mylist[::2])

# you can use slices to reverse a sequence
print("\nSlicing to Reverse")
print(mylist[::-1])

# Tuples are like lists, but they are immutable
print("\nTuples")
mytuple = (0,1,2,"three")
print(mytuple[1])

# Sets are also sequences, but they contain unique values
print("\nSets")
myset = {1, 2, 3, 2, 4, "hey"}
print(myset)


# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print("\nTest for Membership")
print(1 in mylist)
print(3 in mytuple)
print(5 in myset)