# Outer Class:
class Student:
    def __init__(self,name,rollnb):
        self.name = name
        self.rollnb = rollnb

    def show(self):
        print(self.name, self.rollnb)

    # Inner Class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8


s1 = Student('Lolo', 9)
s2 = Student('Tristan', 10)

s1.show()
s2.show()

# creation d'un objet "Inner class" à l'extérieur de la "Outer class"
lap1 = Student.Laptop()
print(id(lap1))

