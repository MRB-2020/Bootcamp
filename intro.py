##Intro to Python
#just going trhough some basic 

print("hello world!!\nLet's lern a new skill\n")
print('We can skip a line on a print') #\n creates a new line in Python


###List
# List is the basic way to declare (create) variables in Python
# Single name for a collection of items in a single variable; can containe any type of values and containe different types in the same list

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, 
# all with different qualities and usage.

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


fam = ['dad',1.85,'mother', 1.76,'son',1.60] # fam list has strings and floats
fam1 = list(('dad',1.85,'mother', 1.76,'son',1.60)) # you can declare a list using list() function

print(fam == fam1) #True

print(f'\n{fam}')

# you slice a list with a [first element - included : second element - excluded]
# Python index starts at zero

print(f'\n{fam[0:4]}')

print(fam[1]) #select the seconf object in the list

# print(fam[1,5]) doesn't worl, you can not select more than one object with a coma

print(fam[0], fam[2], fam[4]) #you can print more than one object using print() command. Add '\n' to generate a new line or ident

print(f'{fam[0]} \n{fam[2]} \n{fam[4]}')

## List methods

# Methods in Python are build in function that are type specific
# the usage is listname.method()

# list.append(x) Add an item (only 1) to the end of the list. Equivalent to list[len(list):] = [x]

fam.append('daughter') 
fam.append(1.65)

print(fam)

# list.extend(iterable) Extend the list by appending all the items from the iterable. Equivalent to list[len(list):] = iterable
# iterable is an object which can be looped or iterated over with the help of a loop (is ordered)

fam1.extend(['daughter',1.65])

print(fam1)

a = list((1,2,3))

a.extend(range(4,11))

print(a)


# list.insert(i,x) Insert an item (only 1) at a given position. i is the index of the element before which to insert x

fam.insert(4, 'daughter') # insert daughter before son
fam.insert(5, 1.79) # insert 1.79 before son

print(fam)


