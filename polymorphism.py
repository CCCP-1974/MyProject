class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:

    def execute(self):
        print("Spell checking")
        print("Convention checking")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):  # ide (Integrated Development Environment)
        ide.execute()
        # question: quel est ici le type de 'ide' ?
        # Le fait qu'il dispose de la méthode execute() indique que 'ide' n'est pas un objet de la classe Laptop
        # (car pas de méthode execute() dans cette classe). 'ide' doit être défini par ailleurs.


ide = MyEditor()
# ici 'ide' est de type 'MyEditor', ce qui ne nous empêche pas de le passer à la méthode code(),
# à la condition que la classe MyEditor possède une methode qui s'appelle 'execute()'

lap1 = Laptop()
lap1.code(ide)




