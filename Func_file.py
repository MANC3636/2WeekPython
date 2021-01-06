

#---------math funcs-------------
def add(x,y):
    print(x+y)
    return x+y

def square (x):
    print(x*x)
    return x*x

def divide (x, y):
    print(x/y)
    return x/y

#let students make a subtract function

#---------string funcs---------------

def get_name():
    name = input("please enter your name: ")
    return name

def use_name(get_name):
    name =get_name()
    print(f"sooo your name is: {name}")

#------------using Turtle---------------

def draw_square(angle, length):
    import turtle
    tt=turtle.Screen()
    t=turtle.Turtle()
    for x in range(4):
        t.fd(length)
        t.lt(angle)
    tt.mainloop()

def multi_draw(desired_shape):
    import turtle
    shape=desired_shape
    if shape =="square":
        draw_square(90, 45)

#make a draw_triangle and then have multi_draw make triangles
#if there is time, modify multi_draw parameters so they can take arguments.