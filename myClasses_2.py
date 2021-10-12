# definition d'une classe
class Computer:
    def config(self): # mot clé 'self' represente l'objet générique de la classe qui appellera la méthode
        print("info du PC: i5, 16Gb RAM, 1TB FLASH")

# creation de deux instances de la classe 'Computer' à l'aide de son constructeur
com1 = Computer()
com2 = Computer()

# pour appeler une méthode, il faut spécifier sa classe d'origine,
# ainsi que l'instance pour laquelle elle est appelée, en guise d'argument
Computer.config(com1)
Computer.config(com2)

# autre possibilité pour appeler une méthode: depuis l'objet lui-même:
com1.config()
com2.config()
