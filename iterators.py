#  Dans ce fichier on présente plusieurs façon de parcourir des listes ou des séquences

# premiere possibilité: boucle for

nums = [7,8,9,5]

print("first way to parse a list: for loop")
for i in nums:
   print(i)

# Autre possibilité: convertir un objet (ici une liste) en iterator à l'aide de la fonction iter()
it = iter(nums)

# Affichage des valeurs de l'iterator à l'aide de la méthode built-in __next__()
print("second way to parse a list: using built-in method of iterator it.__next__()")
print(it.__next__())
print(it.__next__())

# Affichage des valeurs de l'iterator à l'aide de la fonction next() en passant l'iterator en parametre
print("third way to parse a list: using function next(it)")
print(next(it))
print(next(it))


# creation d'iterator "user" (creation d'une classe d'objets "iterables"):
# dans cet exemple on souhaite afficher les 10 premiers entiers

class TopTen:
   def __init__(self):
      print("__init__() executed")
      self.num = 1

   def __iter__(self):
      print("__iter__() executed")
      return self

   def __next__(self):
      print("__next__() executed")
      if self.num <= 10:  # on définit une limite de taille pour l'iterator, sinon la série est infinie.
         val = self.num
         self.num += 1
         return val
      else:
         raise StopIteration  # levée de l'exception "StopIteration" (built-in), seul moyen d'interrompre une boucle



values = TopTen()

# Il existe plusieurs manières d'afficher les valeurs de l'iterator "values"

# 1ere solution: appeler la méthode __next__() définie dans la classe (surcharge)
print("Top ten values using __next__() built-in method:")
print(values.__next__())
print(values.__next__())
print(values.__next__())

# 2eme solution: avec une boucle for
# Mais attention, il faut spécifier une limite à la boucle, sinon elle s'execute indéfiniment
# Cette contrainte est traitée dans la définition de la methode __next__() pour stopper la boucle après la 10ème valeur

for i in values:
   print(i)




