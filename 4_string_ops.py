
#let's create a string file
file="string_file.txt"
author="Bootsy Collins"
a=open(file, "w")
a.write(f"one nation under a groove, getting down just for the funk of it {author}")
a.close()
#----------2, now let's open it and read it
a=open(file, "r")
listing=[a.readline()]
print("nation" in listing[0])

print(listing[0][0:25])
print("nation" in listing[0][26:])

#touch on Booleans, but don't dwell



#let them create their own text files, put text in the file and parse the text

#introduce the following

using_join="-".join("the")
using_replace=listing[0].replace("the","-")
print(using_join)
print(using_replace)
print("nation".find(using_replace[0]))
print(using_replace.split(" "))

#the point is not join, replace, split, nor replace.  The point is: for a container type, the coder has
#a bunch of things she can do
print(dir(str))


