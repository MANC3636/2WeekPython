
#all programming language have a way to store large containers of data
#normally these containers can be decreased, added to, inspected, etc.
#a list is simple to make, assign an empty list to a varible

list1= [] #let's add to the list
print(list1)
list1.append("Harriet")
list1.append("catnip")
list2=[]
print(list1)
#a list can be added to a list
list2.extend(list1)
list2.append("the Raven")
print("this is list2: ", list2); print(f"this is also list2: {list2}")

#we can inspect a list using subscription that we used with strings
#print("this is from list1:", list1[2]) #why didn't this work?
#try
print(list1[0])

#we can pop and remove items from the list:
list1.pop(1)
print("this is list1 with the 2d item popped out: ", list1)
list2.remove("Harriet")
print("this is list2 with Harriet removed: ", list2)

#there is host of things we can do;
print(dir(list))