students = []
import pickle
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

    def writeTxt(self, students):
        file = open ('students.txt','wb')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        pickle.dump("\nStudent list:\n",file)
        for st in students:
            serialized_data = (f"ID: {st['id']}, Name: {st['name']}, DoB: {st['dob']}\n")
            pickle.dump(serialized_data, file)
        file.close()