# Create programs to implement different types of inheritances.
# Inheritance
class Polygon:
    def _init_(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def _init_(self):
        Polygon._init_(self,3)

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)(s-b)(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
print("-------")
# Multiple Inheritance
class Calculation1: 
        def Summation(self,a,b): 
                return a+b
class Calculation2: 
        def multiplication(self,a,b):
                return a*b
class Derived(Calculation1,Calculation2): 
        def divide(self, a, b):
                return a/b
d = Derived() 
print(d.Summation(10, 20))
print(d.multiplication(10, 20))
print(d.divide(10, 20))
print("-------")
#Multi-level Inheritance
class Animal:
        def speak(self):
                print("Animal Speaking")
class Dog(Animal):
        def bark(self):
                print("dog barking")
class DogChild(Dog):
        def eat(self):
                print("Eating bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()