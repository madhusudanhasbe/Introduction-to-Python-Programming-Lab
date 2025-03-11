def add_student():
    L = []
    student_dict = {}

    try:
        name_file = open("student_name.txt", "a")
        mark_file = open("student_marks.txt", "a")
    except:
        name_file = open("student_name.txt", "w")
        mark_file = open("student_marks.txt", "w")

    name = input("\nEnter student name: ")

    name_file2 = open("student_name.txt", "r")
    name_list = name_file2.readlines()

    if f"{name}\n" not in name_list:
        math = float(input("Enter Maths marks: "))
        chem = float(input("Enter Chemistry marks: "))
        phys = float(input("Enter Physics marks: "))
        pyth = float(input("Enter Python marks: "))

        L.append(math)
        L.append(chem)
        L.append(phys)
        L.append(pyth)

        student_dict[name] = L
        name_file.write(name+"\n")
        mark_file.write(f"{math}, {chem}, {phys}, {pyth}\n")

    else:
        print("Student already exists in system")

    main()

def remove_student():
    name = input("Enter student name: ")

    name_file = open("student_name.txt", "r")
    marks_file = open("student_marks.txt", "r")

    name_temp = name_file.read()

    name_list = name_temp.split()

    x = name_list.index(name)
    name_list.remove(name)

    marks_list = marks_file.readlines()

    marks_list.pop(x)
    
    name_file2 = open("student_name.txt", "w")
    marks_file2 = open("student_marks.txt", "w")

    for i in range(0, len(name_list)):
        name_file2.write(name_list[i]+"\n")

        if i == len(name_list) - 1:
            marks_file2.write(marks_list[i]+"\n")
        else:
            marks_file2.write(marks_list[i])

    name_file2.close()
    marks_file2.close()

    name_file.close()
    marks_file.close()
    main()

def calculate_average():
    name = input("\nEnter student name: ")

    name_file = open("student_name.txt", "r")
    marks_file = open("student_marks.txt", "r")

    temp_l = []
    
    name_list = name_file.readlines()
    marks_list = marks_file.readlines()

    try:
        name_index = name_list.index(name+"\n")
    except:
        name_index = name_list.index(name)


    for i in range(0, 4):

        marks = marks_list[name_index].split(",")
        
        if i == 3:
            x = marks[i].rstrip("\n")
            pyth = x.lstrip(",")
            temp_l.append(float(pyth))
        
        else:
            temp_l.append(float(marks[i].rstrip(",")))

    print("The total average marks of "+str(name)+ " = " + str((sum(temp_l)/4)))
    main()

def print_student_list():
    name_file = open("student_name.txt", "r")
    marks_file = open("student_marks.txt", "r")

    name_list = name_file.readlines()

    temp_l = []

    for i in range(0, len(name_list)):
        marks_list = marks_file.readline()
        
        mark_split = marks_list.split(",")

        try:
            print("\nName:",name_list[i].rstrip("\n"))
        except:
            print("\nName:",name_list[i])

        for i in range(0, 4):
            if i == 3:
                x = mark_split[i].rstrip("\n")
                pyth = x.lstrip(",")
                temp_l.append(float(pyth))
            
            else:
                temp_l.append(float(mark_split[i].rstrip(",")))

        
        print("Maths = ",temp_l[0])
        print("Python = ",temp_l[3])
        print("Physics = ",temp_l[2])
        print("Chemistry = ",temp_l[1])
        
    print()
    main()

def main():
    global x
    
    print("\n1. Add student grades")
    print("2. Remove student")
    print("3. Calculate average")
    print("4. Print students")
    print("5. Exit")
    option = int(input("Enter option: "))

    if option == 1:
        add_student()

    elif option == 2:
        remove_student()

    elif option == 3:
        calculate_average()

    elif option == 4:
        print_student_list()

    elif option == 5:
        x = False

    else:
        print("Invalid option")

x = True
while x:
    print("Enter your credentials")
    tr_name = input("\nName: ")
    password = input("Password: ")

    log_file = open("log_creds.txt", "r")
    log_read = log_file.readlines()

    if str(f"{tr_name}:{password}") in log_read:
        print("\n<=====WELCOME TO SYSTEM=====>")
        main()

    elif f"{tr_name}:{password}\n" in log_read:
        print("\n<=====WELCOME TO SYSTEM=====>")
        main()
    
    else:
        print("\nInvalid Login Credentials")
        input("\nPRESS ENTER TO TRY AGAIN")
