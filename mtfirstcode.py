students = list()
def students_saving():
    for student_save in students:
        with open("students.txt", "a") as students_saver:
            students_saver.write("Name: ")
            students_saver.write(student_save)
            students_saver.write("\n")
students_saving()
print("███████╗ ██████╗██╗  ██╗ ██████╗  ██████╗ ██╗         ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██║  ██║██╔═══██╗██╔═══██╗██║         ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
███████╗██║     ███████║██║   ██║██║   ██║██║         ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║   ██║██║   ██║██║         ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                    ")
print("1: Add new student")
print("2: Remove Student")
print("3:Contact Developer")
print("4: Search Student")
choose = int(input("choose a number 1 to 3 only"))
if choose == 1:
    student_name = (input("Enter Student Name to add: "))
    students.append(student_name)
    students_saving()
    print(student_name, "Saved to students file")
elif choose == 2:
    try:
        removed_student_name = (input("Enter Student Name to remove: "))
        students.remove(removed_student_name)
        print(removed_student_name, "removed from the students list: ")
    except ValueError:
        print(removed_student_name, "Not Found in students list:")
elif choose == 4:
    student_search = (input("Enter student name to search"))
    students_file_new = students.copy()
    if students_file_new in students:
        print(student_search, "Found in students list")
    else:
        print(students_file_new, "Not Found in students list")

else:
    print("invalid Number")
