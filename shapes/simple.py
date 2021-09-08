import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

#square
crush.color("red")
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)

#triangle
crush.penup()
crush.goto(-70,-20)
crush.pendown()
crush.color("green")
crush.forward(60)
crush.right(120)

crush.forward(60)
crush.right(120)

crush.forward(60)
crush.right(120)

#hexagon
crush.penup()
crush.goto(-70,70)
crush.pendown()
crush.color("blue")
crush.forward(30)
crush.right(60)
crush.forward(30)
crush.right(60)
crush.forward(30)
crush.right(60)
crush.forward(30)
crush.right(60)
crush.forward(30)
crush.right(60)
crush.forward(30)
crush.right(60)

wn.exitonclick()
wn.mainloop()