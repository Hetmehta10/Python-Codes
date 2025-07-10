# Add constructor in the above class to initialize student details of n students and implement following methods:
# a) Display() student details
# b) Find Marks_percentage() of each student
# c) Display result() [Note: if marks in each subject >40% than Pass else Fail]
# Write a Function to find average of the class
class Student:
    def _init_(self, n):
        self.students = []
        for i in range(n):
            print(f"Enter details for student {i + 1}:")
            name = input("Name: ")
            sap_id = input("SAP ID: ")
            physics_marks = float(input("Physics Marks: "))
            chemistry_marks = float(input("Chemistry Marks: "))
            maths_marks = float(input("Maths Marks: "))

            marks = {'physics': physics_marks, 'chemistry': chemistry_marks, 'maths': maths_marks}

            self.students.append({'name': name, 'sap_id': sap_id, 'marks': marks})

    def display(self):
        print("\nStudent Details:")
        for student in self.students:
            print("Name:", student['name'])
            print("SAP ID:", student['sap_id'])
            print("Physics Marks:", student['marks']['physics'])
            print("Chemistry Marks:", student['marks']['chemistry'])
            print("Maths Marks:", student['marks']['maths'])
            print()

    def find_marks_percentage(self):
        print("\nMarks Percentage:")
        for student in self.students:
            total_marks = sum(student['marks'].values())
            percentage = (total_marks / 300) * 100
            print(f"{student['name']}: {percentage:.2f}%")

    def display_result(self):
        print("\nResult:")
        for student in self.students:
            if all(mark >= 40 for mark in student['marks'].values()):
                print(f"{student['name']}: Pass")
            else:
                print(f"{student['name']}: Fail")

def find_class_average(students):
    total_marks = 0
    total_students = len(students.students)
    for student in students.students:
        total_marks += sum(student['marks'].values())
    class_average = total_marks / (total_students * 3)  # Total subjects = 3
    print(f"\nClass Average Marks: {class_average:.2f}")

n = int(input("Enter the number of students: "))

students = Student(n)

students.display()
students.find_marks_percentage()
students.display_result()

find_class_average(students)