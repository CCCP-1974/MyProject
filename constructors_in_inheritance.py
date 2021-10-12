class A:
    def __init__(self):
        print("init in A")

    def feature_1(self):
        print("feature_1 is working")

    def feature_2(self):
        print("feature_2 is working")


class B(A):
    def feature_3(self):
        print("feature_3 is working")

    def feature_4(self):
        print("feature_4 is working")


class C(A):
    def __init__(self):  # constructeur de la Sub Class C
         print("init in C")

    def feature_5(self):
        print("feature_5 is working")

    def feature_6(self):
        print("feature_6 is working")


class D(A):
    def __init__(self):  # constructeur de la Sub Class D
        super().__init__()  # constructeur de la Super Class A appelé depuis le constructeur de la Sub Class D
        print("init in D")

    def feature_7(self):
        print("feature_7 is working")

    def feature_8(self):
        print("feature_8 is working")


b1 = B()
c1 = C()
d1 = D()

