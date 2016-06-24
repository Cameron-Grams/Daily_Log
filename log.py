def log_study():
    file_type = input("Update an exitisng file (Y/N)?")
    if (file_type == "Y") or (file_type == "y"):
        file_name = (input("Enter file name: "))
        work_file = open(file_name, "r")
        work_string = work_file.read()

    work_array = work_string.split()
    print(work_array)









log_study() 
