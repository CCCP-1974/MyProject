# fonction qui divise 'a' par 'b' sans acun controle des parametres
def div(a,b):
    print("result:", a/b)


# creation d'un "decorator" afin d'assurer que le dividende soit toujours supérieur au diviseur quel que soit l'ordre
# dans lequel sont passés les arguments (si a < b, on inverse a et b), sans modifier la fonction initiale div(a,b)

# fonction qui prend comme argument une autre fonction
def smart_div(func):
    # definition d'une autre fonction à l'intérieur de la fonction smart_div() -- spécificité de Python --
    # qui prend le meme nombre d'arguments que la fonction initiale
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b) # la fonction 'inner' renvoie la fonction initiale avec de nouvelles valeurs pour 'a' et 'b'

    return inner # la fonction smart_div renvoie la fonction 'inner'

# Afin que la fonction smart_div() assure le service, il faut la "connecter" à la fonction initiale div()
# En réalité on assigne "l'ancienne" fonction div() à la "nouvelle" fonction div()
div = smart_div(div)

div(4,2) # dividende > diviseur
div(2,4) # dividende < diviseur
div(9,3) # dividende > diviseur
div(3,9) # dividende < diviseur
div(15,3) # dividende > diviseur
div(3,15) # dividende < diviseur

