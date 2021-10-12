# Dans ce module, on souhaite exécuter deux threads en parallèele, afin d'obtenir un affichage alterné.
# Lorsque les deux threads seront complètement exécutés, on souhaite que le main thread affiche "Bye".
# Pour cela, on fait appel à la méthode join() de la classe Thread qui bloquera l'exécution du main thread tant que
# les deux threads en cours d'exécution n'auront pas atteint leur point de ralliement respectif.

from threading import *
from time import sleep

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

# création de point de ralliement pour les deux threads, avant de poursuivre l'exécution du main thread
t1.join()
t2.join()

# lorsque les deux threads sont terminés, le main thread exécute la dernière instruction
print("From main thread: Bye !")