class student:
    def getNumber(self):
        num_std = 0
        while num_std <= 0:
            num_std = int(input("Enter the number of students: "))
        return num_std   

    def getInfor(self, num_std):
        students=[]
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
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

class course:
    def getNumber(self):
        num_course = 0
        while num_course <= 0:
            num_course = int(input("Enter the number of courses: "))
        return num_course 

    def getInfor(self, num_course):    
        courses=[]
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
    
    def printOut(self, courses): 
        print("\nCourse list:")
        for course in courses:
            print(f"ID: {course['id']}, Name: {course['name']}")

class mark:
    def getInfor(self, students, courses):
        marks={}
        for student in students:
            student_id = student['id']
            std_name = student['name']
            marks[student_id] = {}
            for course in courses:
                course_id = course['id']
                course_name = course['name']
                mark = float(input(f"Enter marks for {std_name} in {course_name}: "))
                marks[student_id][course_id] = mark
        return marks
    
    def printOut(self, students, courses, marks): 
        print(f"\nStudent Information and Marks")
        for student in students:
            student_id = student['id']
            student_name = student['name']
            print(f"\nID: {student_id}, Name: {student_name}")
            for course in courses:
                course_id = course['id']
                course_name = course['name']
                mark = marks.get(student_id, {}).get(course_id, {})
                print(f"Marks in {course_name}: {mark}")

def main():
    students = []
    courses = []
    marks = {}
    student1 = student()
    course1 = course()
    mark1 = mark()

    while True:
        print("\nChoose a function:")
        print("1. Enter number of Students, Students' information, and print out")
        print("2. Number of Courses, Courses' information, and print out")
        print("3. Input Marks and print out")
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

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose again!")
main()       