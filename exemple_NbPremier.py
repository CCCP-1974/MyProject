num = int(input('enter a number: '))

for i in range(2,num):  # la boucle commence après 1 et s'arrête à num-1
    if num % i == 0:
        print(num,': Not prime number')
        break # inutile de tester les autres valeurs
else:
    print(num,'is a prime number')