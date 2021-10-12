# fonction "filter" applique un test binaire (issu d'une fonction définie) à chaque élément d'une séquence

# Exemple: trier les nombres pairs et impairs parmi une liste:
# il faut définir la fonction que l'on souhaite appliquer aux éléments de la liste.
# solution basique: créer une fonction qui réalise le traiment souhaité puis la passer comme argument à la fonction 'filter'

def is_even(n):
    return n%2 == 0 # renvoie un booleen (True ou False)

myList = [2,5,6,9,48,3,15,27,62,78,41,99,121,14,23]

evens = list(filter(is_even,myList)) # ici le résultat de la fonction 'filter' est casté en liste

# amélioration:
# la fonction 'filter' utilise une fonction lambda qui trie les nombres impairs
odds = list(filter(lambda n: n%2==1,myList))

# affichage resultats:
print("liste initiale: ", myList)
print("liste nombres pairs: ", evens)
print("liste nombres impairs: ", odds)


