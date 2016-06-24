class Daily_Log():
    #Daily_Log contains the collection of days of study and the mechanics to represent them

    def __init__(self):
        self.log = []

    def entry(self):
        more_input = True

        while more_input:
            record_month = input("Enter name of month: ")
            date = input("Enter date: ")
            days_hours = eval(input("Enter hours studied: "))
            study_day = Day_of_Study(record_month, date, days_hours)
            self.log.append(study_day)
            additional_records = input("Are there additional days to record? ")
            if additional_records == "no":
                more_input = False

    def report(self):
        hour_log = []
        for day in self.log:
            print(day) 
        for day in self.log:
            hour_log.append(day.hours)
        print(hour_log)


    def master_log(self):
        pass
        #this is where we have to put the data into a file... 






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

log = Daily_Log() 
log.entry()
log.report()
