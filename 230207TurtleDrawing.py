import turtle

tao = turtle.Pen()

tao.shape('turtle')

tao.penup()
tao.goto(-200, 0)
tao.pendown()

tao.pencolor("lightgrey")
for i in range(50):
    tao.forward(50)
    tao.left(123)
    
tao.pencolor("darkgrey")
for i in range(50):
    tao.forward(100)
    tao.right(123)

tao.pencolor("dimgrey")
for i in range(50):
    tao.forward(200)
    tao.left(123)

tao.pencolor("black")
for i in range(50):
    tao.forward(400)
    tao.right(123)

turtle.done()
