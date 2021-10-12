class A:  # classe indépendante
    def __init__(self):  # constructeur de la classe A
        print("init in A")

    def feature1(self):  # methode qui porte le meme nom que la methode de la classe B
        print("feature1_A is working")

class B:  # classe indépendante
    def __init__(self):  # constructeur de la classe B
        print("init in B")

    def feature1(self):  # methode qui porte le meme nom que la methode de la classe A
        print("feature1_B is working")

class C(A,B):  # classe qui hérite des classes A et B
    def __init__(self):  # constructeur de la classe C
        super().__init__()  # const. d'une des deux Super Class --> la première citée dans la déclaration de C(A,B)
        print("init in C")

    def feature2(self):
        print("feature_C is working")


c1 = C()
c1.feature1()
