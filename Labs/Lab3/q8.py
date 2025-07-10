# Print the grade sheet of a student for the given range of CGPA. Scan marks of five subjects and calculate the
# percentage.
# CGPA=percentage/10
# CGPA range:
# 0 to 3.4 -> F
# 3.5 to 5.0->C+
# 5.1 to 6->B
# 6.1 to 7-> B+
# 7.1 to 8-> A
# 8.1 to 9->A+
# 9.1 to 10-> O (Outstanding)
# Sample Gradesheet
# Name: Rohit Sharma
# Roll Number: R17234512 SAPID: 50005673
# Sem: 1 Course: B.Tech. CSE AI&ML
# Subject name: Marks
# PDS: 70
# Python: 80
# Chemistry: 90
# English: 60
# Physics: 50
# Percentage: 70%
# CGPA:7.0
# Grade: A
name=input("Enter name: ")
roll=input("Enter roll: ")
sem=input("Enter sem: ")
sap=input("Enter sap: ")
course=input("Enter course: ")
a=int(input("Enter marks in PDS: "))
b=int(input("Enter marks in Python: "))
c=int(input("Enter marks in Chemistry: "))
d=int(input("Enter marks in English: "))
e=int(input("Enter marks in Physics: "))
percent=(a+b+c+d+e)/5
cgpa=percent/10
if cgpa>=0 and cgpa<=3.4:
        grade='F'
elif cgpa>=3.5 and cgpa<=5:
        grade='C+'
elif cgpa>=5.1 and cgpa<=6:
        grade='B'
elif cgpa>=6.1 and cgpa<=7:
        grade='B+'
elif cgpa>=7.1 and cgpa<=8:
        grade='A'
elif cgpa>=8.1 and cgpa<=9:
        grade='A+'
else:
        grade='O'
print('-------------------')
print('Name : %s\nRoll Number : %s\tSAPID : %s\nSem : %s\tCourse : %s'%(name,roll,sem,sap,course))
print("PDS: %d\nPython: %d\nChemistry: %d\nEnglish: %d\nPhysics: %d"%(a,b,c,d,e))
print('Percentage: %f\nCGPA: %f\nGrade: %s'%(percent,cgpa,grade))