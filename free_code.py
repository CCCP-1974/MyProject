import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
print('sum = ',a+b)

#remarque 1: arg[0] est réservé au nom du fichier lors de l'execution de la commande dans le prompt
#remarque 2: la fonction argv[], capture les caracteres au format 'str'. Pour manipuler ces caracteres sous forme de nombres, il faut les convertir