# Exemple "d'operator overloading":
# Dans ce fichier on souhaite additionner deux objets d'une classe définie par l'utilisateur
# On va définir la méthode __add__(), toujours associée au symbole '+', pour la classe en question
# Remarque: dans d'autres classes, le symbole '+' renvoie toujours à une méthode __add__(), mais celle-ci aura un autre
# comportement (ex: addition dans la classe 'int', concaténation dans la classe 'str', etc)


class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self,other):
        total_self = self.m1 + self.m2
        total_other = other.m1 + other.m2
        if total_self > total_other:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(50,100)
s2 = Student(20,70)
s3 = s1 + s2
# ici, l'operateur '+' appliqué à deux objets de la classe Student est associé à la méthode de classe __add__()
# Remarque: ce lien entre le symbole '+' et le nom de la méthode '__add__()' est figé dans Python
# (impossible d'appeler la méthode 'toto')

print("s3.m1 =",s3.m1)
print("s3.m2 =",s3.m2)


# Autre exemple: comparaison des deux objets s1 et s2 de la classe Student
# On souhaite savoir lequel des deux possède le plus gros total

if s1 > s2:  # l'opérateur '>' est associé à la méthode __gt__(), dont le comportement est défini dans la classe Student
    print("s1 wins")
else:
    print("s2 wins")


# Dernier exemple: On souhaite afficher les objets de la classe Student.
# Si on utilise la fonction print, celle-ci ne va pas retourner les valeurs des attributs d'un objet Student,
# mais seulement les informations sur la classe et l'adresse de l'objet...
# Solution: redéfinition de la fonction __str__() qui caste les variables en chaîne de caractères

# affichage de la valeur d'une variable de type entier
a = 9
print(a)

# vérification que les deux syntaxes sont equivalentes
print(a.__str__())  # renvoie le caractère correspondant à la valeur de la variable, et non son adresse


# Tentative d'affichage des valeurs d'un objet de la class Student
# Les deux syntaxes ci-dessous sont équivalentes (la methode __str__() est appelée dans les deux cas)
print(s1)
print(s1.__str__())