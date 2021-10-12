# En Python, l'utilisation d'opérateurs usuels fait en réalité appel à des méthodes de classes.
# Dans ce fichier, on vérifie que l'utilisation d'un operateur via son symbole (+,-,*,/) est équivalente
# à l'appel de la méthode correspondant à son implémentation

a = 5
b = 6

calcul_1 = a + b
print(calcul_1)

# Le calcul_1 est en réalité implémenté par:
calcul_2 = int.__add__(a,b) # methode __add__() de la classe int
print(calcul_2)

# les deux syntaxes sont équivalentes

# De même avec des variables de type string
c = '5'
d = '6'

calcul_3 = c + d
print(calcul_3)  # dans la classe 'str', le symbole '+' réalise la concaténation de c et d --> '56'

calcul_4 = str.__add__(c,d)
print(calcul_4)  # concaténation de c et d --> '56'