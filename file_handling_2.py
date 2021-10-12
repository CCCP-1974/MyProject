# Dans ce module, on effectue la copie du contenu d'un fichier dans un autre.
# Ce module nécessite que le fichier 'MyData', qui sera accédé en lecture, existe.
# Le fichier destination 'NouveauFichier' (accédé en écriture) peut éventuellement ne pas exister, il sera alors créé

f1 = open('MyData.txt', 'r')
f2 = open('NouveauFichier.txt', 'w')

# Manière simple de copier le contenu d'un fichier vers un autre: boucle for
for data in f1:
    f2.write(data)
# Note:
# Cette méthode fonctionne pour une copie de caractères ASCII, mais ne convient pas pour recopier un contenu binaire
# (image, photo, son...)

# Pour manipuler des fichiers contenant des informations binaires, on utilise les options :
# 'rb' (read binary)
# 'wb' (write binary)

f3 = open('OM_photos.JPG', 'rb')
f4 = open('Copie_OM_photos.JPG', 'wb')

for data in f3:
    f4.write(data)