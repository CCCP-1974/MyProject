# Fonction sans nom, que l'on ne va utiliser qu'une seule fois,
# et qui execute une action simple (comme un calcul élémentaire)

# Exemple de fonction qui calcule le carré d'un nombre

# méthode classique: on définit une fonction puis on l'appelle
def square(n):
    return n * n

result1 = square(5)
print("classic square:",result1)

# méthode utilisant les fonctions "lambda":
f = lambda n : n*n
result2 = f(5)
print("square using lambda:",result2)


# exemple de fonction lambda qui additionne trois nombres:
s = lambda a,b,c : a+b+c
result3 = s(9,11,3)
print("addition using lambda:",result3)


