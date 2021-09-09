import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

for counter in range(4):
  crush.forward(50)
  crush.right(90)

crush.penup()
crush.goto(-70,-70)
crush.pendown()
crush.color("red")
for counter in range(3):
  crush.forward(40)
  crush.right(120)

crush.penup()
crush.goto(-70,70)
crush.pendown()
crush.color("green")
for counter in range(6):
  crush.forward(20)
  crush.right(60)

wn.exitonclick()
wn.mainloop()