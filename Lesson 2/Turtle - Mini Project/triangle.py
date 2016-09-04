#minor changes to thai thien code

import turtle

recursion_depth = 4 #depth of the frectal
triangle_size = 200 #outer triangle size

def draw_triangle(meow,length,recursion):
    recursion=recursion+1
    if (recursion == 1):
        meow.speed(1)
        meow.forward(length/2)
        meow.left(120)
        for i in range(2):
            meow.forward(length)
            meow.left(120)
        meow.forward(length/2)
        meow.left(120)
        meow.speed(10)
        draw_triangle(meow,length/2,recursion)
        
    else:
        for i in range(0,3):
            if(recursion<recursion_depth):
                meow.forward(length/2)
                meow.left(120)
                draw_triangle(meow,length/2,recursion)
                meow.right(120)
                meow.forward(length/2)
            else:
                meow.forward(length)
            meow.right(120)


meow = turtle.Turtle() # init
meow.color("blue","green") # set color5
meow.shape("turtle") # set shape to a turtle
meow.width(2) #line thickness
background = turtle.Screen()  # create background
background.bgcolor("white")     # set background color to red

meow.fill(True) #fill the drawing
draw_triangle(meow,triangle_size,0)
meow.fill(False)

background.exitonclick()      # click anywhere to close background
