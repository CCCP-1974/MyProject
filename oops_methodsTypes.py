# Ce module illustre les notions de méthodes d'instance, méthodes de classe, et méthodes statiques

class Student:

    school = 'esinsa'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

# Méthodes d'instance (mot clé 'self')
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # "Accessor": méthode qui "lit" une variable d'instance
    def get_m1(self):
        return self.m1

    # "Mutator": méthode qui "écrit" une variable d'instance
    def set_m1(self, value):
        self.m1 = value

# Méthode de classe (mot clé 'cls')
    @classmethod  # flag obligatoire pour déclarer une méthode de classe
    def getSchoolName(cls):
        return cls.school

# Méthode statique (ne traite ni variables d'instance ni variables de classe)
    @staticmethod  # flag obligatoire pour déclarer une méthode statique
    def info():
        print("This is the 'Student' class... in 'oops_methodsTypes' module")


s1 = Student(56, 47, 32)
s2 = Student(79, 41, 13)

# deux possibilités d'appeler une méthode statique (depuis la classe ou depuis l'objet)
Student.info()
s1.info()
print("moyenne pour s1:", s1.avg())
print("ecole:", Student.getSchoolName())

