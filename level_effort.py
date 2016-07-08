from graphics import *

class Daily_Log():
    #Daily_Log contains the collection of days of study and the mechanics to represent them

    def __init__(self):
        self.log = []
        self.hour_log = []
        self.work_array = []

    def entry(self):
        more_input = True

        while more_input:
            record_month = input("Enter name of month: ")
            date = input("Enter date: ")
            days_hours = eval(input("Enter hours studied: "))
            study_day = Day_of_Study(record_month, date, days_hours)
            self.log.append(study_day)
            additional_records = input("\nAre there additional days to record? (yes or no)")
            if additional_records == "no":
                more_input = False

    def full_report(self):
        for day in self.log:
            print(day)

    def hour_report(self):
        for day in self.log:
            self.hour_log.append(day.hours)

    def update_record(self):
        file_type = input("Update an exitisng file (Y/N)?")
        if (file_type == "Y") or (file_type == "y"):
            file_name = (input("Enter file name: "))
            work_file = open(file_name, "r")
            work_string = work_file.read()
            self.work_array = work_string.split()
            work_file.close()
        else:
            file_name = (input("Enter name of file to save: "))
        self.hour_report()
        self.work_array = self.work_array + self.hour_log

    def graphic_array(self):
        #this is the array formated for use by Display, a list of ints
        int_array = []
        for initial_hours in self.work_array:
            i = int(initial_hours)
            int_array.append(i)
        return int_array

    def log_array(self):
        #this will be where the file is written out for storage
        pass

    def master_log(self):
        #returns an array of Day_of_Study objects
        return self.log



class Day_of_Study():
    #this object contains the stats of the actual day of stady

    def __init__(self, month, day, hours):
        self.month = month
        self.day = day
        self.hours = hours

    def __str__(self):
        return "On {0} {1} I studied {2} hours.".format(self.day, self.month, self.hours)

    def hours(self):
        return self.hours


class Display():
    #this is the object that develops the display of the log data
    def __init__(self):
        self.win = GraphWin("Time Line", 900, 500)
        self.win.setBackground("#cc9900")
        self.win.setCoords(0,0, 12, 12)

    def configure(self):
        x = Point(0.5,1)
        x2 = Point(11,1)
        y = Point(0.5,11)
        Line(x,y).draw(self.win)
        Line(x, x2).draw(self.win)

        #hours per day scale y-axis
        hour_location = Point(0.25, 1)
        for i in range(13):
            Text(Point(0.25, 1 + i), str(i)).draw(self.win)

        #standard
        xs = Point(0.5, 9)
        xl = Point(11, 9)
        standard = Line(xs, xl)
        standard.draw(self.win)
        standard.setOutline("Red")


    def update(self, array):
        start = 0.5
        increment = 11.5/(len(array))
        p0 = Point(0.5, 9)
        
        for p in array:
            mark = Point(start, p + 1)
            mark.draw(self.win)
            start = start + increment
            progress_line = Line(p0, mark)
            progress_line.draw(self.win)
            p0 = mark            
        

        



def main():
    log = Daily_Log()
    log.entry()
    log.update_record()
    list_hours = log.graphic_array()
    display = Display()
    display.configure()
    display.update(list_hours)
    x = input("Good?")

main()
