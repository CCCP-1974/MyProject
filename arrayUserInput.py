# import de toutes les fonctions du module array
from array import *

# creation tableau vide
arr = array('i',[])

# saisie de la taille du tableau par le user
n = int(input('Enter the length of the array: '))

# remplissage du tableau par le user
for i in range(n):
    x = int(input('Enter the next value: '))
    arr.append(x)
print(arr)

# recherche index d'une valeur dans le tableau
# 1: méthode manuelle (boucle for):
valSearched = int(input('enter te value to search: '))
k=0 # k représente l'index dans le tableau
for e in arr:
    if e == valSearched:
        print(valSearched,'is at index:',k)
        break
    k += 1

# 2: méthode Python
print('using Python method: ',end ='')
print(arr.index(valSearched))

# import de toutes les fonctions du module array
from array import *

# creation tableau 2D
arr2 = array('i',[7,4,3],[2,6,8])
print(arr2)
