# Dans ce module on trie une liste en utilisant la méthode de swapping:
# on compare deux à deux les éléments de la liste et on les inverse si nécessaire,
# puis on compare avec l'élément suivant, et ainsi de suite.
# A la fin de la première itération, la plus grande valeur sera en dernière position
# Pour une liste de taille 'n' il faut n-1 itérations pour trier entièrement la liste.
# L'implémentation de cet algorithme requiert deux boucles:
# - la première parcourt tous les éléments de la liste et réalise le swap
# - la deuxième gère les itérations nécessaires


def sort(list):
    for i in range(len(list)-1,0,-1):  # boucle qui gère les itérations (démarre à 11-1 = 10, s'arrête à 1 (10 iter.)
        for j in range(i):  # boucle qui parcourt les éléments de la liste et réalise le swap si nécessaire
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


nums = [7,23,6,39,55,74,2,78,4,8,9]

sort(nums)
print(nums)

