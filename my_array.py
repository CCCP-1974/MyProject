# il faut importer le modeu array: import array
# on peut également utiliser un alias: import array as arr
# on peut aussi importer seulement la fonction dont on a besoin: from array import array()
# ou bien, on peut importer toutes les fonctions du module array: from array import *

# creation d'un tableau: il faut utiliser la fonction array() et préciser le type des éléments du tableau
# attention: en Python, les types ont des codes: 'i' pour integer; 'h' pour signed short; 'H' pour unsigned short...

from array import *

vals = array('i',[5,9,-1,21,39]) # type 'i': signed int --> le tableau peut donc contenir un entier négatif (mais pas un float)

print(vals)

# le tableau a des méthodes
# par exemple buffer_info qui renvoie l'adresse du tableau et sa taille

print(vals.buffer_info())

# ajout d'une valeur dans le tableau
vals.append(13)
print(vals)

# suppression d'un element: remove
vals.remove(-1)
print(vals)

# inversion des elements du tableau (le premeir devient le dernier, le deuxieme devient l'avant dernier...)
vals.reverse()
print(vals)

# index: on peut cibler une valeur du tableau
print(vals[0])
print(vals[1])

# affichage de toutes les valeurs du tableau une par une:
for i in range(5):
    print(vals[i])

# si on ne connait pas la taille du tableau et qu'on veut afficher tous ces éléments: on utilise len(vals)
for i in range(len(vals)):
    print(vals[i])

# possibilité d'afficher les éléments du tableau sans passer par leur index mais directement par leur valeur:
for e in vals:
    print(e)

# tableau de carcatères: utiliser le code de type 'u' (pour 'unicode')
char_tab = array('u',['A','E','I'])
for c in char_tab:
    print(c)

# possibilité de créer un tableau identique à un autre, sans connaître ni son type, ni ses valeurs:
myArr = array('i',[1,5,8,13,27])
newArr = array(myArr.typecode,(a for a in myArr))
for e in newArr:
    print(e)

# creation d'un tableau qui contient les carrés des valeurs d'un autre tableau:
myArr2 = array('i',[1,2,3,4,5])
newArr2 = array(myArr2.typecode,(a*a for a in myArr2))
for e in newArr2:
    print(e)

# affichage des valeurs d'un tableau à l'aide d'une boucle while (pas tres adaptée car nécessite 3 steps:
# init, test condition, increment
# (dans ce cas une voucle for est plus pratique)

i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1