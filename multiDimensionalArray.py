from numpy import *

# syntaxe: des tableaux dans un tableau
# exemple: tableau 2D
arr1 = array([
                [1,2,3,4,5,6],
                [7,8,9,10,11,12]
            ])
# afficher le tableau
print('array:',arr1)

# afficher le type des data du tableau
print('type:',arr1.dtype)

# afficher le nombre de dimension du tableau
print('nb dim:',arr1.ndim)

# afficher le format du tableau (nb rows vs nb columns)
print('shape:',arr1.shape)

# afficher la taille du tableau (en termes de nombre d'éléments total)
print('size:',arr1.size)

# créer un tableau unidimensionnel à partir d'un tableau multidirectionnel
arr2 = arr1.flatten()
print('unidim:',arr2)

# creation d'un tableau multidimensionnel à partir d'un tab unidimensionnel (preciser nb rows vs nb columns)
arr3 = arr2.reshape(3,4)
print('multidim:\n',arr3)

# creation d'un tableau contenant lui-même deux tableaux de deux lignes et trois colonnes (2x[2x3])
arr4 = arr2.reshape(2,2,3)
print('2x[2x3]:\n',arr4)