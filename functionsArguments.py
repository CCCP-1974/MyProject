# demonstration qu'en Python, un passage d'argument par référence (adresse) n'affecte pas le contenu initial (contrairement aux pointeurs en C)
# les objets "unmutable" ne peuvent pas être modifiés, sinon ils changent d'adresse
def update(x):
    # affichage adresse argument avant traitement
    print("address of 'x' before process:",id(x))
    x = 8
    print ("value of 'x' after process:",x)
    print("address of 'x' after process:", id(x))

print('passing argument through value...')
# passage d'argument par valeur:
update(10)

# sauter une ligne
print()

a = 10
# passage d'argument par reference
print('passing argument through reference...')

# affichage adresse de la variable 'a' avant appel fonction
print("address of 'a' before function call:",id(a))

update(a)

# affichage adresse de la variable 'a' après appel fonction
print("address of 'a' after function call:",id(a))

# affichage valeur variable 'a' après appel fonction
print("value of 'a' after function call:",a)

# sauter une ligne
print()
print('Exemple with mutable object: list')
print()
#####################################################################################################
#####################################################################################################

# meme exemple avec des objets "mutable" (comme une liste)

def updateMutable(list):
    # affichage adresse argument avant traitement
    print("address of 'list' before process:",id(list))
    list[1] = 100
    print ("value of 'list' after process:",list)
    print("address of 'list' after process:", id(list))

print('passing argument through value...')
# passage d'argument par valeur:
updateMutable([10,20,30,40])

# sauter une ligne
print()

myList = [10,20,30,40]
# passage d'argument par reference
print('passing argument through reference...')

# affichage adresse de la variable 'myList' avant appel fonction
print("address of 'myList' before function call:",id(myList))

updateMutable(myList)

# affichage adresse de la variable 'myList' après appel fonction
print("address of 'myList' after function call:",id(myList))

# affichage valeur variable 'myList' après appel fonction
print("value of 'myList' after function call:",myList)





