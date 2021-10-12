# Ce module illustre la notion de "variables de classe" vs "variables d'instance"
# variable d'instance:
# --> propre à chaque objet créé, initialisée dans la methode __init__, et modifiable individuellement
# variable de classe:
# --> commune à tous les objets créés, initialisée en dehors de la methode __init__, la modif affecte tous les objets

class Car:
    # class variables
    nbRoues = 4

    def __init__(self):
        # instance variables
        self.marque = "BMW"
        self.kilometrage = 10000

# instanciation de deux objets de classe Car
c1 = Car()
c2 = Car()

# affichage initial apres création objets
print(c1.marque, c1.kilometrage, c1.nbRoues)
print(c2.marque, c2.kilometrage, c2.nbRoues)

# on peut modifier une variable d'instance d'un objet sans affecter les autres objets
c2.kilometrage = 15000
print(c1.marque, c1.kilometrage, c1.nbRoues)
print(c2.marque, c2.kilometrage, c2.nbRoues)

# modification variable de classe --> affecte tous les objets
Car.nbRoues = 3

print(c1.marque, c1.kilometrage, c1.nbRoues)
print(c2.marque, c2.kilometrage, c2.nbRoues)

