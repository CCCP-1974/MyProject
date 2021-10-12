# Outer Class:
class Student:
    def __init__(self,name,rollnb):
        self.name = name
        self.rollnb = rollnb
        self.lap = self.Laptop()  # creation d'un objet "Inner class" à l'intérieur de la "Outer class"

    def show(self):  # méthode 'show()' appartenant à la classe 'Student'
        print(self.name, self.rollnb)
        self.lap.show()

    # Inner Class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):  # méthode 'show()' appartenant à la classe 'Laptop'
            print(self.brand, self.cpu, self.ram)


s1 = Student('Lolo', 9)
s2 = Student('Tristan', 10)

s1.show()


