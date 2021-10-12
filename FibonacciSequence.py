# afficher les 'n' premiers nombres de la sequence de Fibonacci
# Rappel: sequence Fibonacci: 0 1 1 2 3 5 8 13 21 34 ... (on ajouet les deux derniers nombres pour calculer le suivant)

def fib(n):
    a = 0
    b = 1

    # traitement du cas particulier
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            # calcul du nombre suivant
            c = a + b

            # shift des nombres
            a = b
            b = c
            print(c)

x = int(input('enter the end limit of the series: '))
fib(x)