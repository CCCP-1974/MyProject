## Dans ce module on recherche un élément particulier dans une liste et on affiche son index si l'élément est trouvé

# Liste des éléments à parcourir
liste_a_trier = [1,7,9,4,6,8]

# Index de l'élément s'il est trouvé dans la liste (initialisé à -1).
# Variable globale pour être éventuellement réutilisée par une autre fonction si besoin
pos = -1

# La fonction qui effectue la recherche
def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i  # Syntaxe necessaire pour accéder à la variable globale
                                   # Cette syntaxe permet d'utiliser une variable locale du même nom dans la fonction
            return True
        else:
            i += 1
    return False

if search(liste_a_trier, 9) == True:
    print("Searched value found at index:", pos)
else:
    print("Searched value not found...")