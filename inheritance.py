# Ce module traite de la notion d'héritage de classe (Inheritance).
# Héritage simple niveau (A -> B), et héritage multi-niveau (A -> B -> C)
# Héritage multiple (A,B -> C)

# Définition classe A qui possède deux méthodes
class A:
    def feature_1(self):
        print("feature_1 is working)")

    def feature_2(self):
        print("feature_2 is working)")

# Définition classe B qui hérite de la classe A
# Note: La classe B possède deux méthodes qui lui sont propres (feature_3() et feature_4())
#       ainsi que les méthodes héritées de la classe A (feature_1() et feature_2())

class B(A):
    def feature_3(self):
        print("feature_3 is working)")

    def feature_4(self):
        print("feature_4 is working)")

# Définition classe C qui hérite de la classe B
# Note: La classe C possède une méthode propre (feature_5())
#       ainsi que les méthodes héritées des classes A et B (feature_1(), feature_2(), feature_3() et feature_4())
class C(B):
    def feature_5(self):
        print("feature_5 is working)")

# Définition classe indépendante, avec une méthode
class D:
    def feature_6(self):
        print("feature_6 is working)")

# Définition classe indépendante, avec une méthode
class E:
    def feature_7(self):
        print("feature_7 is working)")

# Définition d'une classe qui hérite des classes D et E (HERITAGE MULTIPLE)
class F(D,E):
    def feature_8(self):
        print("feature_8 is working)")

# création objet classe A
a1 = A()
# appels des deux méthodes disponibles
a1.feature_1()
a1.feature_2()

# création objet classe B
b1 = B()
# appels des deux méthodes propres à la classe B
b1.feature_3()
b1.feature_4()
# appels des deux méthodes héritées de la classe A
b1.feature_1()
b1.feature_2()

# création objet classe F
f1 = F()
# appel de la méthode propre à la classe F
f1.feature_8()
# appel de la méthode héritée de la classe D
f1.feature_6()
# appel de la méthode héritée de la classe E
f1.feature_7()

