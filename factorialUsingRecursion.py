def fact(n):
    # cas particulier: fin de la chaîne
    if n == 0:
        return 1
    res = n * fact(n-1)
    return res


# saisie clavier d'un nombre puis appel de la fonction fact() qui utilise le principe de la récursivité pour
# calculer la factorielle (au lieu d'une boucle for étudiée dans un exemple précédent)
x = int(input("enter a number: "))
result = fact(x)
print('{}! = {}'.format(x,result))
