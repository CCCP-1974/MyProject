# La fonction 'map' modifie tous les éléments d'une liste en leur appliquant une fonction passée en argument
# Exemple: tripler les valeurs d'une la liste

myList = [2,5,6,9,48,3,15,27,62,41,14,23]
triples = list(map(lambda n : n*3, myList)) # il faut caster le résultat de 'map' en liste

# affichage resultats:
print("liste initiale: ", myList)
print("liste des valeurs triplées: ", triples)
