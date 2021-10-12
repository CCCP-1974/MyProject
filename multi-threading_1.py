# Dans ce module, on essaie d'exécuter deux threads à tour de rôle.
# Pour cela, il faut faire appel au module "threading" afin que les méthodes respectives ne s'exécutent pas de manière
# séquentielle, ainsi qu'au module "time" pour ralentir l'exécution du code, sans quoi, l'intégralité du thread serait
# exécuté pendant le premier créneau alloué par l'OS (car il s'agit dans cet exemple d'un mini thread très court)

# PREMIERE PARTIE:
# on ne fait pas appel aux modules 'threading' et 'time' --> les methodes s'exécutent l'une après l'autre

class Hello:
    def run(self):
        for i in range(5):
            print("Hello")

class Hi:
    def run(self):
        for i in range(5):
            print("Hi")

t1 = Hello()
t2 = Hi()

t1.run()
t2.run()

