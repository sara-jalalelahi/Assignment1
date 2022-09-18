import turtle as tu
side=int(input('enter side :'))
color=input('enter color :')
size=int(input('enter side length :'))
tu.pencolor(color)
for i in range (side):
    tu.left(360/side)
    tu.forward(size)
tu.exitonclick()










