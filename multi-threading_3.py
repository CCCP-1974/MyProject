# Dans ce module, on essaie d'exécuter deux threads à tour de rôle.
# Pour cela, il faut faire appel au module "threading" afin que les méthodes respectives ne s'exécutent pas de manière
# séquentielle, ainsi qu'au module "time" pour ralentir l'exécution du code, sans quoi, l'intégralité du thread serait
# exécuté pendant le premier créneau alloué par l'OS (car il s'agit dans cet exemple d'un mini thread très court)

# TROISIEME PARTIE:
# on fait appel aux modules 'threading' et 'time' --> les methodes s'exécutent en tant que threads, et on temporise
# les exécutions des deux threads pour leur laisser le temps d'alterner: sleep(1).
# De même, on place une légère tempo entre les deux démarrage pour désynchroniser les deux threads, afin qu'ils ne se
# réveillent pas au même moment (collision)

from threading import *
from time import sleep

# les classes Hello et Hi héritent de la classe Thread:
# elles bénéficient donc de toutes ses méthodes dont start() et run(); run() est la méthode démarrée par start()
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()  # Pour démarrer l'exécution du thread, on appelle la méthode start() qui est associée à la méthode run()
sleep(0.2)  # On retarde le démarrage du deuxième thread pour les désynchroniser (afin d'éviter les collisions)
t2.start()

