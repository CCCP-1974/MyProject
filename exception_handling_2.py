# dans ce module on teste l'interception de plusieurs types d'erreurs à l'aide des mots-clé correspondant

a = 9

try:
    b = int(input("Enter a number: "))
    print("a/b =", a/b)
except ZeroDivisionError as e:
    print("Hey ! You cannot divide a number by Zero ! -->", e)
except ValueError as e:
    print("Invalid user entry -->", e)
except Exception as e:
    print("Something went wrong... -->", e)
finally:
    print("End of 'try' block. Bye")

