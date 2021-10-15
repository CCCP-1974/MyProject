## Dans ce module on recherche un élément particulier dans une liste et on affiche son index si l'élément est trouvé

# Liste des éléments à parcourir
sortedList = [4,7,8,12,45,99,133,245,612,1974]
searchedValue = int(input('Please, enter the value to search: '))
# Index de l'élément s'il est trouvé dans la liste (initialisé à -1).
# Variable globale pour être éventuellement réutilisée par une autre fonction si besoin
pos = -1

# La fonction qui effectue la recherche
def search(list, n):
   l = 0  # lower boundary
   u = len(list)-1  # upper boundary

   while l <= u:
       mid = (l+u) // 2  # division entière: // (ici on ne veut pas de nombre à virgule)

       if sortedList[mid] == n:
           globals()['pos'] = mid
           return True
       else:
           if sortedList[mid] < n:
               l = mid+1
           else:
               u = mid-1
   return False  # gère le cas où la valeur recherchée ne se trouve pas dans la liste



if search(sortedList, searchedValue) == True:
    print("Searched value found at index:", pos)
else:
    print("Searched value not found...")