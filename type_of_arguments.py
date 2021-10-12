def person1(name,age):
    print(name)
    print(age)

# pour éviter les confusions lors de l'appel de la fonction
# (du genre: person(46,'lolo')), on peut utiliser la syntaxe qui fait appel à la notion de 'Keyword':
person1(age = 46, name = 'lolo')
# Dans ce cas, on peut modifier l'ordre des arguments par rapport au prototype de la fonction.

# Valeur par défaut d'un paramètre:
def person2(name,age = 19):
    print(name)
    print(age)

# appel de fonction en passant les deux arguments attendus
person2('Tit',25)
# appel de fonction en ne passant qu'un seul des deux arguments attendus
person2('Tit')


# Notion de "variable length": le nombre d'arguments passés à la fonction peut varier
# --> faire précéder le paramètre de '*'

def sum(*b):
    print('b:',b)
    c = 0
    for i in b:
        c += i
    print('c:',c)

sum(4,8,13,6,7)


# Keyworded variable length arguments
def person3(name, **data):
    print('name:',name)

    # affichage de chaque élément de 'data':
    for i,j in data.items():
        print(i,j)


person3('lolo', age = 46, birthplace = 'marseille', phone = 123456)

