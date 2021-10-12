from numpy import *

arr1 = array([1,2,3,4,5])

# afficher le tableau
print(arr1)

# afficher le type des éléments du tableau
print(arr1.dtype)

# linspace (contraction de "linear" et "space") prend 3 arguments (start, stop (inclus), nb de parts)
arr2 = linspace(0,15,16)
print(arr2)
print(arr2.dtype)

# arange (contraction de array() et range()): prend 3 arguments (start, stop (exclus), step)
arr3 = arange(1,15,2)
print(arr3)
print(arr3.dtype)

# logspace (contraction de "logarithm" et "space") prend 3 arguments (start, stop (inclus), nb de parts)
arr4 = logspace(1,40,5)
print(arr4)
print(arr4.dtype)
print('%.2f' %arr4[4])

arr5 = zeros(5) # format 'float' par defaut
arr6 = zeros(5,int) # format 'int' spécifié
arr7 = ones(5) # format 'float' par defaut
arr8 = ones(5,int) # format 'int' spécifié

print(arr5)
print(arr6)
print(arr7)
print(arr8)

arr9 = array([1,2,3,4,5])
arr9 = arr9 + 5
print(arr9)

arr10 = array([0,2,4,6,8])
arr11 = array([1,3,5,7,9])
arr12 = arr10 + arr11
print(arr12)

# afficher sinus, cosinus, log de chaque élément du tableau arr1, puis somme, elem min, elem max...
print('sinus:',sin(arr1))
print('cosinus:',cos(arr1))
print('log:',log(arr1))
print('somme:',sum(arr11))
print('minimum:',min(arr11))
print('maximum:',max(arr11))

#concatenation
print('arr8:',arr8)
print('arr9:',arr9)
print('concatenation arr8 & arr9:',concatenate([arr8,arr9]))

# exemple de copie d'un tableau "shadow copy" (les tableaux sont liés l'un à l'autre)
# un changement de valeur dans un tableau affecte l'autre tableau également
arr12 = array([23,24,25,26,27])
arr13 = arr12.view()
# modification d'une valeur d'un tableau après copie
arr12[3]=100
print('arr12:',arr12)
print('arr13:',arr13)
print('add arr12:',id(arr12))
print('add arr13:',id(arr13))

# exemple de copie d'un tableau "deep copy" (les tableaux ne sont pas liés l'un à l'autre)
# un changement de valeur dans un tableau n'affecte pas l'autre tableau --> utiliser méthode copy()
arr14 = array([10,11,12,13,14])
arr15 = arr14.copy()
# modification d'une valeur d'un tableau après copie
arr14[3]=99
print('arr14:',arr14)
print('arr15:',arr15)
print('add arr14:',id(arr14))
print('add arr15:',id(arr15))