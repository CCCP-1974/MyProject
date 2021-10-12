# fonction qui récupère une liste passée par l'utilisateur puis affiche le compte de nombres pairs et impairs
# Subtilité: un test est effectué sur les entrées clavier pour éliminer celles qui ne sont pas des entiers

def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd


lst = []
while True:
    userInput = input("--> ").strip()
    if userInput == '':
        # on quitte la boucle si la valeur est vide
        break
    else:
        # on tente une conversion du caractère saisi en int (la valeur saisie est peut-être un str ou un float)
        try:
            lst.append(int(userInput))
        except ValueError: # mot clé de Python
            print('previous entry discarded ! please enter an integer value')
# appel de la fonction principale
even, odd = count(lst)
# affichage du résultat en appliquant une méthode de formatage qui appartient au type 'str'
print("even numbers: {} and odd numbers: {}".format(even,odd))