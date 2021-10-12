# Dans cet exemple, on simule une machine qui delivre des bonbons
# Si la quantité demandée est inférieure au stock, les bonbons sont fournis
# sinon, on renvoie un message d'avertissement et on quitte la boucle

stock = 10
desiredNb = int(input('How many candies do you want ? '))
i = 1

while i <= desiredNb:
    if desiredNb > stock:
        print('there are not',desiredNb,'candies in the machine')
        break
    print('Candy')
    i+=1
print('Bye')