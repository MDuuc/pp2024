import numpy as np
import math

marks = {} 

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
        if isinstance(students, dict): 
            students = [students]
        sorted_students = sorted(students, key=lambda x: x.get('gpa', 0), reverse=True)
        return sorted_students