# Exemple de Method Overloading (meme nom, nb d'arguments differents) interdit en Python
# class Student:
#    def sum(self, a):
#        s = a
#        return s
#
#    def sum(self, a, b):
#        s = a+b
#        return s
#
#    def sum(self, a, b, c):
#        s = a+b+c
#        return s
#
# s1 = Student()
# print(s1.sum(7))

# En Python on peut passer un nombre d'arguments variable aux méthodes (et donc reproduire un comportement de
# Method Overloading) à l'aide du mot clé 'None'

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a

        return s


s1 = Student(50,60)

#  print("9 =",s1.sum(9))
#  print("7 + 8 =",s1.sum(7,8))
#  print("1 + 5 + 7 =",s1.sum(1,5,7))


class A:
    def show(self):
        print("hello from class A")


class B(A):
    def show(self):
        print("hello from class B")


b = B()
b.show()