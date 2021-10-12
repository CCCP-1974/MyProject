# La fonction 'reduce' traite tous les éléments d'une séquence pour aboutir à un résultat unique
# Dans cet exemple: tous les elements de la liste sont additionnés
# Rappel: le traitement des données s'effectue par accumulation, sur des valeurs consécutives
# (il faut donc definir une fonction qui traite deux valeurs et qui sera propagée sur tous les éléments)
# La fonction 'reduce' appartient au module 'functools'
from functools import reduce

# Premiere solution: définition et appel de fonction classique
def addAll(a,b):
    return a+b

myList = [2,5,6,9,48,3,15,27,62,78,41,99,121,14,23]

sum1 = reduce(addAll, myList) # ici, pas de cast en liste car le résultat est une valeur unique
print('somme par solution 1: ',sum1)

# solution avec fonction Lambda:
sum2 = reduce(lambda a,b : a+b, myList)
print('somme par solution 2: ', sum2)
