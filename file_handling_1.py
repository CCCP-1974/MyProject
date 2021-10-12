# Dans ce module on accède à des fichiers en lecture et en écriture pour y stocker des données de manière permanente

# Ouverture du fichier 'MyData' en lecture
# 'f' devient lui même un objet de type 'file', et à ce titre il possède certaines méthodes

f = open('MyData', 'r')

# Tentative de lire le contenu du fichier 'f' qui a été affecté du fichier 'MyData'
# L'instruction ci-dessous va en réalité afficher les propriétés de l'objet fichier mais pas son contenu
print(f)

# Pour accéder au contenu du fichier, on fait appel à sa méthode read() qui fetch les data
#print(f.read())

# D'autres méthodes de fichier permettent d'autres options:

# Afficher seulement une ligne: methode readline()
# Cette méthode possède un pointeur in-built qui est géré automatiquement afin d'afficher les lignes suivantes.
# Dans ce code, les instructions ci-dessous seront sans effet car un affichage intégral du fichier a déjà été effectué
# auparavant par print(f.read() et le pointeur se situe à la fin du fichier.

print(f.readline())  # affichage première ligne
print(f.readline())  # affichage ligne suivante
print(f.readline())  # affichage ligne suivante

# astuce, pour ne pas que la fonction print insère un saut de ligne alors que le fichier lui-même en contient déjà,
# on utilise l'option end=""
print(f.readline(), end="")  # affichage ligne suivante sans sauter de ligne supplémentaire
print(f.readline(), end="")  # affichage ligne suivante sans sauter de ligne supplémentaire


# Accès en écriture

# 1ère étape: ouverture du fichier en écriture (le fichier n'existe pas, il sera créé par Python)
f1 = open('NouveauFichier', 'w')

# 2ème étape: écriture(s) dans le fichier à l'aide de la méthode write()
# Note: lorsque le fichier est ouvert en écriture, on peut y écrire autant de fois qu'on le souhaite, les data
# seront écrites les unes à la suite des autres.
# Par contre, si on ouvre ce même fichier en écriture une autre fois avec l'option 'w',
# on va écraser les données précédentes.
# Pour conserver les données présentes dans le fichier, lors du deuxième accès, il faudra l'ouvrir avec
# l'option 'a' (append) pour écrire les nouvelles données à la suite des précédentes.

f1.write("Hello, je m'appelle Laurent. ")
f1.write("Je suis une formation de Python. ")
f1.write("Jusque-là, ça me plait... ")

f1 = open('NouveauFichier', 'a')
f1.write("Et je confirme. ")

# Manipulation de fichiers: copier le contenu du fichier MyData dans le fichier NouveauFichier


