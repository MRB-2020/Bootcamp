##Intro to Python
#just going trhough some basic 

print("hello world!!\nLet's lern a new skill\n")
print('We can skip a line\n on a print') #\n creates a new line in Python

##########
###List###
##########


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


##################
## List methods ##
##################

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

# list.remove(x) Remove the first tem form the list whose value is equial to x. It raises a ValueError if there is no such item

fam.remove('daughter')

print(fam)

# list.pop(i) Remove the item at the given position in the list, and return it. 
# If no index is specified, a.pop() removes and returns the last item in the list.

fam.pop(4) # removes 1.79

print(fam)

# list.clear() Remove all items from the list. Equivalent from del list[:]

fam.clear() 

print(fam)


# list.copy() Return a shallow copy of the list.

fam = fam1.copy() #copy method only copy the values of the list not the object it self.

print(fam)

fam[3] = 1.78 # change in the copy does not affect the original list as declaring fam = fam1 would

print(fam == fam1) #false

fam2 = fam

fam2[3] = 1.76 #change of a value in one list changes the other list aswell

print(fam == fam2) #True

# list.index() returns the position at the first occurrence of the specified value.

print(fam.index('son'))


# list.count(x) Return the number of times x appears in the list.

print(fam.count('mother')) # 1

fam1.extend(['daughter',1.65])
print(fam1.count('daughter')) # 2

print(fam.count(1.50)) # 0


# list.sort() sort the list (if the list has the same type of values) ascending by default. 
# You can also make a function to decide the sorting criteria(s).

# print(fam.sort()) does not work it has floats and strs

heights = list((fam[1], fam[3], fam[5]))
relations = list((fam[0], fam[2], fam[4]))

print(heights)
print(relations)

heights.sort()
relations.sort(reverse=True)

print(heights)
print(relations)

# list. reverse() Reverse the elements of the list in place.

fam.reverse()
print(fam)


### List Comprehention ###
##########################

# List comprehension offers a shorter syntax when you want to create a new list based on the specific values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  # want to creat a nee list with only fruit with letter "a" 
newlist = []  #empity list

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# list comprehension allows you to accomplish that without the for loop

newlist =[]

print(newlist)
newlist = [x for x in fruits if "a" in x]

print(newlist)


###Tuples###

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

thistuple = ('apple', 'banana', 'cherry')

print(thistuple)

# Tuple items are ordered (can not change its original order), unchangeable, and allow duplicate values.
# you can convert a tuple to a list and them add, delete or update tuple


################
##Dictionaries##
################


# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
    
    
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)   


# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

x = thisdict["model"]

# You can add a item to the dictionary by entering a new key

thisdict['color'] = 'red' # create a new paired entry 'color':'red'

print(thisdict)

# Make changes by assigning new value for existing keys

thisdict['year'] = 2020

print(thisdict)

# Delete a key entry or the whole dictionary with "del"

del thisdict['color'] # deletes the key entry "color" and the value "red"

del thisdict #delete the distionary completely

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# You can loop through a dictionary using a for loop. The return values are the keys

for x in thisdict:
  print(x)              #print the keys
  print(thisdict[x])    #print the values


# Make a copy of a dictionary with "disct()" function

mydict = dict(thisdict)


# Nested dictionaries. A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

myfamily['child1'] #all value inside dictionary child1

myfamily['child1']['year'] #the value of key "year" in dictionary child1



########################
## Dictionary methods ##
########################

# dict.pop()
# dict.clear()
# dict.copy()
# Are methods that work on list also and do the same function


# dict.fromkeys(key, value)  Returns a dictionary with the specified keys and value. It is a way to create or partialy copy a dictionary
# All keys get the same set of values

x = ('key1', 'key2', 'key3')
y = ('entrance', 'garage', 'kitchen door')
newdict = dict.fromkeys(x,y)

print(newdict) # all keys have "('entrance', 'garage', 'kitchen door')" as value. If you want each key to get a unique value you need declare each value for a key

# dict.get(key) Returns the vlaie of a Key item

print(thisdict.get('model')) # print the value of key: model of thisdict dictionary

# dict.items() Returns a view object as a tuple of all key:item pairs in a dictionary

thisdict.items()

# dict.keys() returns a view object with all the keys in a dictionery

thisdict.keys()

# dict.popitem() Removes the last inserted key-value pair

thisdict['color'] = 'red'

thisdict.popitem()

print(thisdict)

# dict.setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the value

thisdict.setdefault("model", "Bronco") # Does change thisdict since the key model already exist
thisdict.setdefault("color", "white") # Creates a new key-value pair = color-white

# dict.update({key:value}) Updates the dictionary with the specified key-value pairs

thisdict.update({'year':2020}) #changes the valeu of key year to 2020
 
# dict.values() Returns a view object. The view object contains the values of the dictionary, as a list.

thisdict.values()