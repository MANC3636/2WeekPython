#send this as an email; ask students to cut and paste into code
text ="so far we've built loops and conditionals but we have not \
combined them to get more computing power.  With nesting,\
watching spacing is key to readable and working code.  \
In C++ and similar languages, they use curly braces to do the same thing"

for x in text:
    if "C++" in text:
        print("it's here")
        break #show what happens without break

#now we can do all sorts of things
#---------------2---------------------
list1=list(text.split(" "))
print("combined" in list1)

#print(list1)
for x in list1:
    if "combined" == x:
        print(f"{x} is in text")
#---------------------2-----------------
#let's go back to our old friend, the dice; for the next example,
#make sure the students watch their spacing.
import Nine_Conditionals
print(Nine_Conditionals.die1); print(Nine_Conditionals.die2)
if Nine_Conditionals.die1==1:
    if Nine_Conditionals.die2==1:
        print("we have snake eyes, a loser")
#ask them to make a conditional that will find some winners (7 and 11)
#----------------------extra------------------------------------------
import random #normally imports should be near line 1
choices=(True, False)

for x in "four":
    path_clear = random.choice(choices)
    if path_clear ==True:
        print("the character can move forward")

        path_to_left = random.choice(choices)
        if path_to_left ==True:
            print("I will turn left")
        else: print("I'm moving forward")
    else:
        print("your character has bumped into a wall")
        break


