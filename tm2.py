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
#        print(self.hour_log)

    def update_record(self):
        file_type = input("Update an exitisng file (Y/N)?")
        if (file_type == "Y") or (file_type == "y"):
            file_name = (input("Enter file name: "))
            work_file = open(file_name, "r")
            work_string = work_file.read()
            self.work_array = work_string.split()
#            print(work_array)
            work_file.close()
        else:
            file_name = (input("Enter name of file to save: "))

        self.hour_report()
        self.work_array = self.work_array + self.hour_log
#        print(self.work_array)


    def graphic_array(self):
        int_array = []
        for initial_hours in self.work_array:
            i = int(initial_hours)
            int_array.append(i)
        return int_array

    def log_array(self):
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

log = Daily_Log()
log.entry()
log.full_report()
print("*****")
log.update_record()
print(log.graphic_array())
