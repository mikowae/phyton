import turtle
nbrsides = 6
for steps in range (nbrsides):
    turtle.forward(100)
    turtle.right(360/nbrsides)
    for moresteps in range(nbrsides):
        turtle.forward(50)
        turtle.forward(360/nbrsides)

