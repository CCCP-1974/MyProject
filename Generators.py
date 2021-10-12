# Dans ce fichier on définit un generator (genre de fonction qui renvoie un iterator), ce qui permet d'obtenir un
# iterator sans gérer manuellement les methodes __iter__() et __next__()

def topten():
    yield 5  #  'yield' est le mot-clé caractéristique du 'generator'


values = topten() #  le résultat de l'appel du generator topten() est un iterator (values)


# si l'on affiche 'values', les info du generator apparaitront (pas la valeur 5)
print("printing the generator info:")
print(values)

# pour afficher la valeur de l'iterator, on utilise la methode __next__(), qui est automatiquement disponible,
# sans besoin de la créer (c'est le principe du generator)
print("printing the value of the iterator using method __next__():")
print(values.__next__())  #  ici, un seul appel de __next__() est possible, car une seule valeur dans le generator

####################### AUTRE EXEMPLE ###############################################

print("next example (generator with 4 values):")
def fourFirstNumbers():
    yield 1
    yield 2
    yield 3
    yield 4

print("printing the 2 first values of the iterator using method __next__():")
num = fourFirstNumbers()
print(num.__next__())
print(num.__next__())

print("printing remaining values of the iterator using for loop:")
# autre possibilité pour afficher les valeurs de l'iterator: la boucle for
for i in num:
    print(i)

####################### AUTRE EXEMPLE ###############################################
print("another generator example: print the 10 first perfect square values")

def square():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq  #  ici, yield renvoie la valeur souhaitée, mais à la différence de 'return', ne termine pas la fonction
        n += 1


tenSquares = square()

for i in tenSquares:
    print(i)


