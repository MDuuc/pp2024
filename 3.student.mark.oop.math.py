import numpy as np
import math


students = []
courses = []
marks = {} 
credits = [] 
class student:
    def getNumber(self):
        while True:
            try:
                num_std = int(input("Enter the number of students: "))
                if num_std > 0:
                    return num_std
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def getInfor(self, num_std):
        for i in range (num_std):
            print(f"\nEnter information for student #{i + 1}:")
            __std_id = input("Student ID: ")
            __std_name = input ("Student name: ")
            __std_dob = input ("Date of birth: ")

            std_info = {
                "id" : __std_id,
                "name" : __std_name,
                "dob": __std_dob 
            }
            students.append(std_info)
        return students
    
    def printOut(self, students):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        print("\nStudent list:")
        for st in students:
            print(f"ID: {st['id']}, Name: {st['name']}, DoB: {st['dob']}")

class course:
    def getNumber(self):
        while True:
            try:
                num_course = int(input("Enter the number of courses: "))
                if num_course > 0:
                    return num_course
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def getInfor(self, num_course):    
        for i in range (num_course):
            print(f"\nEnter information for course #{i + 1}:")
            course_id = input("Course ID: ")
            course_name = input ("Course name: ")

            course_info = {
                "id" : course_id,
                "name" : course_name
            }
            courses.append(course_info)
        return courses
    
    def get_credits(self, courses):
        for i, course in enumerate(courses):
            credit = float(input(f"Enter credits for {course['name']}: "))
            credits.append(credit)
        return np.array(credits)
    
    def printOut(self, courses): 
        print("\nCourse list:")
        for course in courses:
            print(f"ID: {course['id']}, Name: {course['name']}")

class mark:
    def getInfor(self, students, courses):
        for student in students:
            student_id = student['id']
            std_name = student['name']
            marks[student_id] = {}
            for course in courses:
                course_id = course['id']
                course_name = course['name']
                in_mark = float(input(f"Enter marks for {std_name} in {course_name}: "))
                mark = math.floor(in_mark*10)/10
                marks[student_id][course_id] = mark
        return marks
    
    def printOut(self, students, courses, marks): 
        print(f"\nStudent Information and Marks")
        for st in students:
            student_id = st['id']
            student_name = st['name']
            print(f"\nID: {student_id}, Name: {student_name}")
            for course in courses:
                course_id = course['id']
                course_name = course['name']
                mark = marks.get(student_id, {}).get(course_id, {})
                print(f"Marks in {course_name}: {mark}")
    
    def cal_gpa(self, marks, credits):
        students_gpa = {}

        for student_id, student_marks in marks.items():
            marks_array = np.array(list(student_marks.values()))

            if marks_array.shape[0] == 0:
                continue

            reshaped_credits = np.reshape(credits, (1, -1))
            weighted_sum = np.sum(marks_array * reshaped_credits, axis=1)
            total_credits = np.sum(credits)
            average_gpa = np.floor(np.sum(weighted_sum) / total_credits * 10) / 10

            students_gpa[student_id] = average_gpa

        return students_gpa

    def add_gpa(self, students, students_gpa):
        for st in students:
            student_id = st['id']
            gpa = students_gpa.get(student_id)
            if gpa is not None:
                st['gpa'] = gpa

    def desc_gpa(self, students):
        sorted_students = sorted(students, key=lambda x: x.get('gpa', 0), reverse=True)
        return sorted_students
    


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
    print("0. Exit")

    choice = int(input("Choose the number: "))

    if choice == 1:
        num_std = student1.getNumber()
        students = student1.getInfor(num_std)
        student1.printOut(students)

    elif choice == 2:
        num_course = course1.getNumber()
        courses = course1.getInfor(num_course)
        course1.printOut(courses)
        credits = course1.get_credits(courses)

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

    elif choice == 4:
        if not marks:
            print("Please enter marks first (choose option 3).")
            continue

        students_gpa = mark1.cal_gpa(marks, credits)
        mark1.add_gpa(students, students_gpa)
        for student in students:
            print(f"Student ID: {student['id']}, GPA: {student.get('gpa', 'N/A')}")

    elif choice == 5:
        if not marks:
            print("Please enter marks first (choose option 3).")
            continue

        sorted_students = mark1.desc_gpa(students)
        print("\nStudent list sorted by GPA descending:")
        for s in sorted_students:
            print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}, GPA: {s.get('gpa', 'N/A')}")

    elif choice == 0:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose again!")
   