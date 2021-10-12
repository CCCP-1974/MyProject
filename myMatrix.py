from numpy import *
# création d'une matrice à partir de tableaux
arr1 = array([
                [1,2,3,6],
                [4,5,6,7]
            ])

m1 = matrix(arr1)
print(m1)
print(type(m1))

# creation de matrice depuis des chaînes de caractères (2 rows, 4 columns)
m2 = matrix('1 2 3 6 ; 4 5 6 7')
print(m2)
print(type(m2))

# creation de matrice depuis des chaînes de caractères (4 rows, 2 columns)
m3 = matrix('1 2; 3 6 ; 4 5 ;6 7')
print(m3)
print(type(m3))

# creation de matrice depuis des chaînes de caractères (3 rows, 3 columns)
m4 = matrix('1 2 3 ; 4 5 6 ;7 8 9')
print(m4)


# quelques exemples de méthodes de matrices disponibles:
print('diagonal values of m4:',diagonal(m4))
print('min value:',m4.min())
print('max value:',m4.max())

m5 = matrix('2 4 6 ; 8 10 12 ; 14 16 18')
m6 = matrix('1 3 5 ; 7 9 11 ; 13 15 19')
print('m5:')
print(m5)
print('m6:')
print(m6)
m7 = m5 + m6
m8 = m5 * m6
print('sum:')
print(m7)
print('mult:')
print(m8)

