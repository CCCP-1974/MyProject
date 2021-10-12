# Continue permet de ne pas executer les instructions restantes dans la boucle,
# mais la boucle reprend un nouveau cycle pour l'index suivant

# exemple: afficher les nombres de 1 à 100 sauf multiples de 3 et multiples de 5
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i,'',end='')