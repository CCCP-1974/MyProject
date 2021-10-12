# Ex1:
for i in range(4):          # i = [0;3]
    for j in range(4):      # i = [0;3]
        print('# ',end='')  # affiche 4 symboles sur une même ligne
    print()                 # retour à la ligne

print()                     # sauter une ligne entre deux patterns

# Ex2:
for i in range(1,5):        # i = [1;4]
    for j in range(i):      # j = [1;4]
        print('# ',end='')  # affiche i symboles sur une même ligne
    print()                 # retour à la ligne

print()                     # sauter une ligne entre deux patterns

# Ex3:
for i in range(4):
    for j in range(4-i):
        print('# ',end='')
    print()