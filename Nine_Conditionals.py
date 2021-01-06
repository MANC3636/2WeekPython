import random
left = 1
right =2
top =3
bottom=4

list_of_randoms=[left, right, top, bottom]
#for our purposes if a fact == the condition, then the statement is True
#if the statement is True, the code will run.
position=random.choice(list_of_randoms)
print(f"this is position {position}")
#let's see if our randomly generated fact == the condition.
mouse_pos=right
if mouse_pos==position:
    print("the mouse has escaped")
#let them run the code 5-10 times; now let them improve the code:
if mouse_pos==position:
    print("the mouse has escaped")
else: print("the mouse has been caught")
#get them to see that if position is 2, then mouse_pos and position are ==,
#and that therefore mouse_pos==position.  Help them to set up two dice.

die1=random.randrange(1,7); die2=random.randrange(1,7)
roll1=die1 + die2; print(f"this is die1 ({die1}), and this is die2 ({die2}).")
print(roll1)
if roll1==7:
    print("we won")
#let's improve the game
if roll1==7 or roll1==11:
    print("we won")
#let's improve it more:
snakeeyes=2
if roll1==7 or roll1==11:
    print("we won")
elif roll1==snakeeyes:#snakeyes is rare
    print("we lost")

#walk them through the pseudocode for a simple conditional
#if roll1 is 7 or 11,then print("we won")
#break it down
#if the roll1 ==7 or roll1 ==11:
# (spaced properly) print("we won")
