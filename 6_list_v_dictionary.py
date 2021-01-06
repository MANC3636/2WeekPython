#lists are great if you know the index number
#but, that's not the way people think
#we think by association: mother: mother's name; summer: hot; granma: sweets
#keyword: value pairs
#dictionaries give us another way to make containers
#------------1--------------
dict1={}
dict1["grammy"]="chocolate"
dict1["mother"]="mom's name"
dict1["summer"]="hot"
print(dict1)
#----------------2--------------
#let's see how to use dictionaries; let's to go dir
print(dir(dict))
#---------------3--------------------
#let's explore get, pop, keys and values

dict1.pop("grammy")
print(dict1)
#we didn't mean to pop grammy, let's return it and then 'get' grammy
dict1["grammy"]="grammy's name"
print(dict1.get("grammy"))
#-----------4--------------------------------
#try to get the values and the keys
print("keys first: ", dict1.keys(), " and then values:", dict1.values())

#you can iterate over a dictionary to get the keys, the values, or both
for key in dict1:
    print(key, end=" "); print(dict1[key])