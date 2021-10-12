# creation de fonctions


# definitions de fonctions
def myFunction():
    print("Hello there")
    print("Good morning")

def add(x,y):
    c = x+y
    print(x,'+',y,'=',c)

# exemple de fonction qui renvoie une valeur
def returnAdd(x,y):
    c = x+y
    return c

# exemple de fonction qui renvoie deux valeurs
def addSub(x,y):
    c = x+y
    d = x-y
    return c,d

# appels de fonctions
myFunction()
add(4,5)
result = returnAdd(7,3)
print (result)
sum,sub = addSub(13,10)
print(sum,sub)
