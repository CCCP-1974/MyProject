# Dans ce module on trie une liste en utilisant la méthode de sélection (un seul swap par itération)
# A chaque itération on initialise la valeur min (ou max selon le choix) de la liste comme étant la première valeur,
# puis on compare avec les éléments suivants, et la valeur min (ou max, selon choix) est réactualisée si nécessaire.
# Lorsque toute la liste est parcourue, on réalise un seul et unique swap entre la première valeur de l'itération et
# la valeur min (ou max) détectée.
# Cette méthode permet de trier progressivement la liste en ne réalisant qu'un seul swap (gourmand en ressources)
# par itération


def sort(list):
    for i in range(10):  # boucle qui gère les itérations
        minpos = i
        for j in range(i,11):  # boucle qui parcourt les éléments de la liste
            if list[j] < list[minpos]:
                minpos = j

        # à la fin de l'itération, on réalise le swap
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

        print(list)


nums = [7,23,6,39,55,74,2,78,4,8,9]

sort(nums)
print(nums)

