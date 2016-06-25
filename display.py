from graphics import *

class Display:

    def __init__(self, array):
        self.array = array
        self.win = GraphWin("Time Line", 900, 500)
        self.win.setBackground("#cc9900")
        self.win.setCoords(0,0, 12, 12)

    def display(self):
        x = Point(0.5,1)
        x2 = Point(11,1)
        y = Point(0.5,11)
        Line(x,y).draw(self.win)
        Line(x, x2).draw(self.win)

        #hours per day scale y-axis
        hour_location = Point(0.25, 1)
    #    hour = 0
        for i in range(13):
            Text(Point(0.25, 1 + i), str(i)).draw(self.win)

        #standard
        xs = Point(0.5, 8)
        xl = Point(11, 8)
        standard = Line(xs, xl)
        standard.draw(self.win)
        standard.setOutline("Red")


    def update(self):
        start = 0.5
        increment = 11.5/(len(self.array))
        for p in self.array:
            mark = Point(start, p)
            mark.draw(self.win)
            start = start + increment
        x = input("Good?")



# #make this update...
#     #this will have to be the log function
#     a = eval(input("hours studied: "))
#     d = 1
#     log = True
#     while log:
#         Point(d, a).draw(win)
#         d += 1
#         a = eval(input("hours studied: "))
#         if a == 0:
#             log = False
#
#     quit = input("Quit? ")

array = [9, 8, 9, 7]
d = Display(array)
d.display()
d.update()
