# Instructions non critiques: affectation de variables
a = 5
b = 2
c = 0

# Instruction critique: une division peut générer une erreur si le diviseur vaut '0'
# On place l'instruction critique dans un bloc 'try' qui permet de gérer les exceptions qui pourraient se produire
try:
    print(a/b)
except Exception:
    print("Hey, You cannot divide a number by Zero !")

try:
    print(b/a)
except Exception as e:  # ici on souhaite associer l'exception à la variable 'e'
    print("Hey, You cannot divide a number by Zero !", e)  # affichage de la variable (qui correspond au type d'except.)

# bloc 'try' avec 'finally'
try:
    print("A resource has been opened")
    print(b/c)
except Exception as exc:   # ici on souhaite associer l'exception à la variable 'exc'
    print("Hey, You cannot divide a number by Zero !", exc)  # affichage de la variable exc (type d'exception)
finally:
    print("The resource has been closed")

print("Bye")
