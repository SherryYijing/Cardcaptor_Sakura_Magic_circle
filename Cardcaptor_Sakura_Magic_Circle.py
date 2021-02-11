import turtle as t
def circle(x, y, z):
    t.seth(0)
    y = y - z
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(z)

def line(R, r, count, angle):
    t.seth(90 + angle)
    for i in range(count):
        t.penup()
        t.goto(0, 0)
        t.fd(r)
        t.pendown()
        t.fd(R-r)
        t.left(360/count)

def slash(R, r):
    interval = 10
    t.seth(90)
    big = pow((R**2)*2, 0.5)
    small = big-2*interval
    for i in range(13):
        #bigger line
        t.penup()
        t.goto(0, 0)
        t.fd(R)
        t.pendown()
        t.right(135)
        t.fd(big)
         #smaller line
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd(pow((small**2)/2, 0.5))
        t.pendown()
        t.right(135)
        t.fd(small)
        #bold line
        t.pensize(8)
        t.pencolor("black")
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd((R + pow((small**2)/2, 0.5)) / 2)
        t.pendown()
        t.right(135)
        t.fd((big+small) / 2)
        t.pensize(2)
        t.pencolor("yellow")
        t.seth(90+i*30)
    else:
        #bigger line
        t.penup()
        t.goto(0, 0)
        t.fd(R)
        t.right(135)
        t.fd(big / 2)
        t.pendown()
        t.fd(big / 2)
         #smaller line
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd(pow((small**2)/2, 0.5))
        t.right(135)
        t.fd(small / 2)
        t.pendown()
        t.fd(small / 2)
        #bold line
        t.pensize(8)
        t.pencolor("black")
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd((R + pow((small**2)/2, 0.5)) / 2)
        t.right(135)
        t.fd((big+small) / 2/2)
        t.pendown()
        t.fd((big+small) / 2/2)
        t.pensize(2)
        t.pencolor("yellow")
        t.seth(90+i*30)

def star(r, angle):
    t.fillcolor("black")
    t.penup()
    t.goto(0, 0)
    t.seth(90+angle)
    t.fd(r)
    t.pendown()
    t.right(18)
    t.begin_fill()
    for i in range(5):
        t.right(144)
        t.forward(144)
        t.left(72)
        t.forward(144)
    t.end_fill()
    if angle != 0:
        t.seth(90+angle)
        for i in range(1, 6):
            t.penup()
            t.goto(0, 0)
            t.left(72)
            t.pendown()
            t.fd(r)
def moon():
    R = 109
    r = R - 21

    #populate
    t.penup()
    t.goto(-350+2*R, 0)
    t.seth(90)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(R, 359)
    t.left(90)
    t.fd(2)
    t.left(90)
    t.circle(-r, 359)
    t.left(90)
    t.fd(2)
    t.pendown()
    t.end_fill()

    #shape
    circle(-350+R, 0, R)
    circle(-350+44+r-2, 0, r-2)

def seaweed1(r, i):
    t.fillcolor("black")
    t.penup()

    if i == 0:
        t.goto(256, r)
    elif i == 1:
        t.goto(256-r, 0)
    else:
        t.goto(256, -r)
    t.pendown()
    t.begin_fill()
    t.seth(2+i*90)
    t.circle(r/2, 105)
    t.left(10)
    t.circle(-r / 3, 90)
    t.circle(r / 3, 60)
    t.left(20)
    t.circle(r / 3, -80)
    t.left(50)
    t.circle(-r + 10, -40)
    t.right(30)
    t.circle(r / 2 + 10, -50)
    t.penup()
    if i == 0:
            t.goto(256, r)
    elif i == 1:
        t.goto(256 - r, 0)
    else:
        t.goto(256, -r)
    t.pendown()
    t.end_fill()


    t.seth(2 + i * 90)
    t.circle(r / 2, 105)
    t.left(10)
    t.circle(-r / 3, 90)
    t.begin_fill()
    t.circle(r / 3, 60)
    t.left(20)
    t.circle(r / 3, -80)
    t.left(50)
    t.circle(-r + 10, -40)
    t.right(30)
    t.circle(r / 2 + 10, -50)
    t.right(30)
    t.circle(r / 2 - 2, 110)
    t.circle(-r / 3, 70)
    t.left(7)
    t.circle(r / 3, 85)
    t.end_fill()

    t.penup()
    if i == 0:
        t.goto(256, r)
        t.pendown()
        t.seth(180 - (2 + i * 90))
        t.circle(-(r / 2), 105)
    elif i == 1:
        t.goto(256 - r, 0)
        t.pendown()
        t.seth(- (2 + i * 90))
        t.circle(-(r / 2), 105)
    else:
        t.goto(256, -r)
        t.pendown()
        t.seth(180 - (2 + i * 90))
        t.circle(-(r / 2), 105)
    t.begin_fill()
    t.left(-10)
    t.circle(-(-r / 3), 90)
    t.circle(-(r / 3), 60)
    t.left(-20)
    t.circle(-(r / 3), -80)
    t.left(-50)
    t.circle(-(-r + 10), -40)
    t.right(-30)
    t.circle(-(r / 2 + 10), -50)
    t.end_fill()

    t.penup()
    if i == 0:
        t.goto(256, r)
        t.pendown()
        t.seth(180 - (2 + i * 90))
        t.circle(-(r / 2), 105)
    elif i == 1:
        t.goto(256 - r, 0)
        t.pendown()
        t.seth(- (2 + i * 90))
        t.circle(-(r / 2), 105)
    else:
        t.goto(256, -r)
        t.pendown()
        t.seth(180 - (2 + i * 90))
        t.circle(-(r / 2), 105)
    t.pendown()

    t.left(-10)
    t.circle(-(-r / 3), 90)
    t.circle(-(r / 3), 60)
    t.left(-20)
    t.begin_fill()
    t.circle(-(r / 3), -80)
    t.left(-50)
    t.circle(-(-r + 10), -40)
    t.right(-30)
    t.circle(-(r / 2 + 10), -50)
    t.right(-30)
    t.circle(-(r / 2 - 2), 110)
    t.circle(-(-r / 3), 70)
    t.left(-7)
    t.circle(-(r / 3), 85)
    t.end_fill()

def seaweed2(r,i):
    t.penup()
    t.goto(256 + r, 0)
    t.seth(-90)
    t.circle(-r,20)
    t.pendown()
    t.begin_fill()
    t.seth(30)
    t.circle(-r/3,100)
    t.circle(r/6,140)
    t.circle(-r/11,100)
    t.left(80)
    t.circle(-r/2,-30)
    t.circle(r/4,-140)
    t.circle(-r/3,-60)
    t.end_fill()
    t.penup()
    t.goto(256 + r, 0)
    t.seth(-90)
    t.circle(-r, 30)
    t.pendown()
    t.seth(45)
    t.circle(-r / 4, 100)
    t.right(20)
    t.circle(r / 4, 140)
    t.right(10)
    t.circle(-r / 11, 90)

    t.penup()
    t.goto(256 + r, 0)
    t.seth(90)
    t.circle(r, 20)
    t.pendown()
    t.begin_fill()
    t.seth(-30)
    t.circle(-(-r / 3), 100)
    t.circle(-(r / 6), 140)
    t.circle(-(-r / 11), 100)
    t.left(-80)
    t.circle(-(-r / 2), -30)
    t.circle(-(r / 4), -140)
    t.circle(-(-r / 3), -60)
    t.end_fill()
    t.penup()
    t.goto(256 + r, 0)
    t.seth(90)
    t.circle(r, 30)
    t.pendown()
    t.seth(-45)
    t.circle(-(-r / 4), 100)
    t.right(-25)
    t.circle(-(r / 4), 140)
    t.right(-10)
    t.circle(-(-r / 11), 90)

def triangle():
    #big triangle
    t.fillcolor("black")
    for i in range(1, 4):
        t.penup()
        t.goto(256, 0)
        t.seth(i*90)
        t.pendown()
        t.begin_fill()
        t.right(22.5)
        t.fd(50)
        if i==1:
            t.goto(256,3*50-3)
            t.goto(256,0)
            t.seth(i*90+22.5)
            t.fd(50)
            t.goto(256,3*50-3)
        elif i==2:
            t.goto(256- 3 * 50+3,0)
            t.goto(256, 0)
            t.seth(i * 90 + 22.5)
            t.fd(50)
            t.goto(256-3 * 50+3,0)
        else:
            t.goto(256, -3 * 50+3)
            t.goto(256, 0)
            t.seth(i * 90 + 22.5)
            t.fd(50)
            t.goto(256, -3 * 50+3)
        t.end_fill()
    #small triangle
    x = pow(((2 * 50) ** 2) / 2, 0.5)-8
    for i in range(1,5):
        t.penup()
        t.goto(256, 0)
        t.seth(i * 90)
        t.pendown()
        t.begin_fill()
        t.right(22.5)
        t.fd(50)
        if i==1:
            t.goto(256+x,x)
            t.goto(256,0)
            t.right(45)
            t.fd(50)
            t.goto(256+x,x)
        elif i==2:
            t.goto(256 - x, x)
            t.goto(256, 0)
            t.right(45)
            t.fd(50)
            t.goto(256 - x, x)
        elif i==3:
            t.goto(256 - x, -x)
            t.goto(256, 0)
            t.right(45)
            t.fd(50)
            t.goto(256 - x, -x)
        else:
            t.goto(256 + x, -x)
            t.goto(256, 0)
            t.right(45)
            t.fd(50)
            t.goto(256 + x, -x)
        t.end_fill()
        
def special_circle(x, y, z):
    t.fillcolor("black")
    t.begin_fill()
    t.seth(0)
    y = y - z
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(z)
    t.end_fill()
   
def sun():
    seaweed1(50, 0)
    seaweed1(50, 1)
    seaweed1(50, 2)
    seaweed2(50, 3)
    triangle()
    special_circle(256, 0, 50)   

def set_char(s):
    t.penup()
    t.fd(-19)
    t.left(90)
    t.fd(2)
    t.pendown()
    t.write(s, font=["KaiTi", 30, "bold"])

def constellation():
    r = 250
    t.penup()
    t.goto(20, -35)
    t.seth(-45)
    t.fd(r)
    t.pendown()
    constellations = ['♒','♓','♈','♉','♌','♍','♎','♏']
    for i in range(4):
        t.write(constellations[i], font=("", 20, ""))
        t.penup()
        t.right(90)
        t.circle(-300, 30)
        t.left(90)
        t.pendown()
    t.penup()
    t.goto(-r/4+10, 5)
    t.seth(135)
    t.fd(r)
    for i in range(4, 8):
        t.write(constellations[i], font=("", 20, ""))
        t.penup()
        t.right(90)
        t.circle(-300, 30)
        t.left(90)
        t.pendown()

if __name__ == "__main__":
    #initialize
    t.setup(800, 800, 0, 0)
    t.speed(0)
    t.bgcolor("black")
    t.pencolor("yellow")
    t.pensize(2)
    
    #draw biggest circle
    circle(0, 0, 350)
    circle(0, 0, 325)
    circle(0, 0, 321)
    circle(0, 0, 306)
    line(321, 306, 72, 0)

    #draw small circle
    circle(0, 0, 204)
    circle(0, 0, 200)
    circle(0, 0, 186)
    line(200, 186, 72, 0)

    #square frame and line
    line(290, 213, 12, 0)
    line(248, 205, 12, 15)
    slash(306, 204)

    #inner star
    star(200, 36)

    #moon
    moon()

    #sun
    sun()

    #smallest circle
    special_circle(0, 328, 22)
    set_char("北")
    special_circle(0, -328, 22)
    set_char("南")
    special_circle(-328, 0, 22)
    set_char("西")
    special_circle(328, 0, 22)
    set_char("東")

    #outside star
    star(200, 0)

    #constellation
    constellation()
    t.penup()
    t.goto(-500, -500)
    t.pendown()
    t.done()
    
