import zipfile
import os
import pickle
from domains.courses import course
from domains.marks import mark
from domains.students import student

student1 = student()
course1 = course()
mark1 = mark()

while True:
    print("\nChoose a function:")
    print("1. Enter number of Students, Students' information, and print out")
    print("2. Number of Courses, Courses' information, and print out")
    print("3. Input Marks and print out")
    print("4. Calculate average GPA")
    print("5. Show GPA with descended order")
    print("6. Zip into a file")
    print("7. Decompress and deserialize  the file")
    print("0. Exit")

    choice = int(input("Choose the number: "))

    if choice == 1:
        num_std = student1.getNumber()
        students = student1.getInfor(num_std)
        student1.printOut(students)
        student1.writeTxt(students)

    elif choice == 2:
        num_course = course1.getNumber()
        courses = course1.getInfor(num_course)
        course1.printOut(courses)
        credits = course1.get_credits(courses)
        course1.writeTxt(courses)

    elif choice == 3:
        if not students:
            print("Please enter student information first (choose option 1).")
            continue

        if not courses:
            print("Please enter course information first (choose option 2).")
            continue

        num_std = len(students)
        num_course = len(courses)

        marks = mark1.getInfor(students, courses)
        mark1.printOut(students, courses, marks)
        mark1.writeTxt(students, courses, marks)

    elif choice == 4:
        if not marks:
            print("Please enter marks first (choose option 3).")
            continue

        students_gpa = mark1.cal_gpa(marks, credits)
        mark1.add_gpa(students, students_gpa)
        for students in students:
            print(f"Student ID: {students['id']}, GPA: {students.get('gpa', 'N/A')}")

    elif choice == 5:
        if not marks:
            print("Please enter marks first (choose option 3).")
            continue

        sorted_students = mark1.desc_gpa(students)
        print("\nStudent list sorted by GPA descending:")
        for s in sorted_students:
            print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}, GPA: {s.get('gpa', 'N/A')}")

    elif choice == 6:
        with zipfile.ZipFile('students.zip','w') as z:
            z.write('students.txt')
            z.write('courses.txt')
            z.write('marks.txt')

    elif choice ==7:
        if os.path.exists('students.zip'):
            with zipfile.ZipFile('students.zip', 'r') as z:
                z.extractall()
                file_list = z.namelist()
                print("Files in the zip archive are decompress:")
                for file_name in file_list:
                    print(file_name)

                try:
                    with open ('students.txt', 'rb') as s:
                        loaded_data_s = pickle.load(s)
                    print (loaded_data_s)                        
                    with open ('courses.txt', 'rb') as c:
                        loaded_data_c = pickle.load(c)
                    print (loaded_data_c)
                    with open ('marks.txt', 'rb') as m:
                        loaded_data_m = pickle.load(m)
                    print (loaded_data_m)      
                except FileNotFoundError:
                    print("Did not find the file")
        else:
            print ("Please enter input's information")
    elif choice == 0:
        print("Exiting the program. ")
        break

    else:
        print("Invalid choice. Please choose again!")
   