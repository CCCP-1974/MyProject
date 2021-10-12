# definition d'une classe
class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu # creation d'un attribut 'cpu' qui reçoit la valeur cpu passée lors de l'instanciation
        self.ram = ram # creation d'un attribut 'ram' qui reçoit la valeur ram passée lors de l'instanciation

    def config(self): # mot clé 'self' represente l'objet générique de la classe qui appellera la méthode
        print("info du PC: cpu {}, {} Gb RAM".format(self.cpu, self.ram))

# creation de deux instances de la classe 'Computer' à l'aide de son constructeur
com1 = Computer('ARM',16)
com2 = Computer('DSP',32)

# on appelle la méthode depuis l'objet lui-même
com1.config()
com2.config()
