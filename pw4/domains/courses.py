import numpy as np
courses = []
credits = [] 
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