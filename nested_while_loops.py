i = 1
while i<=5:
    print('ligne',i,':',end='') # le dernier argument du print permet de continuer à afficher sur la même ligne
    j=1
    while j<=10:
        print(j,'',end='')
        j+=1

    i+=1
    print('') # pour changer de ligne
