#chars and strings: intro to containers
#we need computers to help humans analyze large amounts of data, which are held in containers
#today we will work with strings; this will form the basis for our later work with lists and dictionaries
# a char is a value like an int is a value; but a string is a container
#new function: len()
a="a"
print (a)
print (len(a))
print(len("a"))
#------------2-------------
b = "a", "b"
print(b)#what is the len of the variable b
print(len(b))
#---------------3---------------
print(len("ab"))
b="the cat in the hat comes back"
print("the len of b is: ", len(b), "is a space counted?")
#-------------4--------------------
#for any container, we can count the items, increase the container, decrease the container, find an item in a container
new_b= "hey diddle diddle, the cat is in the fiddle"
c=(b + new_b)
print(new_b[0])
print(new_b[:2])
print(new_b[0:3])
#ask them to get parts of new_b, words, the first part, the second part

#now ask them to put the new value in a variable

#