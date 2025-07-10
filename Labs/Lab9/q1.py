# Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by taking inputs from the user and
# display details of all students
class Student:
        def _init_(self, name, sap_id, marks):
                self.name = name
                self.sap_id = sap_id
                self.marks = marks
        def show(self):
                print("--------------------------------------------------")
                print(f"Name: {self.name}\nSap_id: {self.sap_id}\nPhy: {self.marks[0]}\nChem: {self.marks[1]}\nMaths: {self.marks[2]}")


students = []
for i in range(3):
        s={'name': None, "Sap_id": None, 'Marks': []}
        s['name'] = input("Enter name: ")
        s['Sap_id'] = input("Enter sap_id: ")
        s['Marks'].append(input("Enter Marks in Phy: "))
        s['Marks'].append(input("Enter Marks in Chem: "))
        s['Marks'].append(input("Enter Marks in Maths: "))
        students.append(s)

student1 = Student(students[0]['name'], students[0]['Sap_id'], students[0]["Marks"])
student2 = Student(students[1]['name'], students[1]['Sap_id'], students[1]["Marks"])
student3 = Student(students[2]['name'], students[2]['Sap_id'], students[2]["Marks"])
student1.show()
student2.show()
student3.show()