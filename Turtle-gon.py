import turtle
side=int(input("Enter sides"))
interior_angles=(side-2)*180/side
for i in range(side):
    turtle.forward(100)
    turtle.left(180-interior_angles)