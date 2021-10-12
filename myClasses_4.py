# definition classe
class People:
    def __init__(self):
        self.name = 'laurent'
        self.age = 46

    def displayConfig(self):
        print(self.name, '-->', self.age)

    def updateConfig(self):
        self.age = 47

    def compareConfig(self, other):
        if self.name == other.name:
            return True
        else:
            return False

# Instanciation de deux objets de la classe 'People'
# A ce stade, la methode __init__ est exécutée pour chaque objet, ils ont donc les memes valeurs d'attributs
people1 = People()
people2 = People()

# affichage des adresses de chaque objet
print('Adresse 1er objet:',id(people1))
print('Adresse 2er objet:',id(people2))

# affichage des attributs des objets créés
print('Avant mise à jour:')
print('Objet 1: ',end = '')
people1.displayConfig()
print('Objet 2: ',end = '')
people2.displayConfig()

# Appel methode 'updateConfig(self)' pour modifier un attribut
# Note: ici, on choisit de le faire de manière statique, sans passer d'argument
people2.updateConfig()

# affichage des attributs des objets après mise à jour
print('Après mise à jour Objet 2:')
print('Objet 1: ', end='')
people1.displayConfig()
print('Objet 2: ', end='')
people2.displayConfig()

# comparaison de l'attribut 'name' entre deux objets de la classe 'People'
# Ici, people1 sera associé à 'self' car c'est lui qui appelle la méthode,
# et people2 sera le deuxième parametre
if people1.compareConfig(people2):
    print('--> Same name')
else:
    print('--> Different name')

