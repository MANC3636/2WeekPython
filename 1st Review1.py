import turtle as t
#--------------1-------
window=t.Screen()
t=t.Turtle()
#-------------2--------
print(dir(t))
#------------3----------
t.write("cat", True, "left")
#---------4-------------------
x=20
y=90
for target in "cat":
    t.write(target, True, "left")
    t.goto(x, y)
    x+=200
#-----------5--------------
#play with some of the turtle commands as you show them loops and strings
#suggested turtle commands include: goto, up, down, fd, bk, left (lt), right (rt), circle
#they can make quite a few geometric shapes, but the shapes should be controlled.

window.mainloop()