from graphics import *

def display():
    win = GraphWin("Time Line", 900, 500)
    win.setBackground("#cc9900")
    win.setCoords(0,0, 12, 12)

    x = Point(0.5,1)
    x2 = Point(11,1)
    y = Point(0.5,11)
    Line(x,y).draw(win)
    Line(x, x2).draw(win)

    #hours per day
    hour_location = Point(0.25, 1)
#    hour = 0
    for i in range(13):
        Text(Point(0.25, 1 + i), str(i)).draw(win)

    #standard
    xs = Point(0.5, 8)
    xl = Point(11, 8)
    standard = Line(xs, xl)
    standard.draw(win)
    standard.setOutline("Red")


    #this will have to be the log function
    a = eval(input("hours studied: "))
    d = 1
    log = True
    while log:
        Point(d, a).draw(win)
        d += 1
        a = eval(input("hours studied: "))
        if a == 0:
            log = False

    quit = input("Quit? ")






display()
