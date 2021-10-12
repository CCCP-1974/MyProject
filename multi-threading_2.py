# Dans ce module, on essaie d'exécuter deux threads à tour de rôle.
# Pour cela, il faut faire appel au module "threading" afin que les méthodes respectives ne s'exécutent pas de manière
# séquentielle, ainsi qu'au module "time" pour ralentir l'exécution du code, sans quoi, l'intégralité du thread serait
# exécuté pendant le premier créneau alloué par l'OS (car il s'agit dans cet exemple d'un mini thread très court)

# DEUXIEME PARTIE:
# on fait appel au module 'threading' mais pas au module 'time' --> les methodes s'exécutent en tant que threads mais
# cela n'est pas visible à l'affichage car le premier thread sera complètement exécuté avant d'avoir démarré le deuxième

from threading import *

# les classes Hello et Hi héritent de la classe Thread:
# elles bénéficient donc de toutes ses méthodes dont start() et run(); run() est la méthode démarrée par start()
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")


t1 = Hello()
t2 = Hi()

t1.start()  # Pour démarrer l'exécution du thread, on appelle la méthode start() qui est associée à la méthode run()
t2.start()  # Pareil pour l'autre thread

