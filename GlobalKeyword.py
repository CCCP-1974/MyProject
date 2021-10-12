# scope des variables: var locale vs var globale

a = 10
print("initial value of global variable 'a' prior funct() call:",a)
print("address of global variable 'a':",id(a))
print()

def funct():
    a = 9
    print('local a =',a)
    print('local address:',id(a))
    print()

    x = globals()['a']
    print("x (image of global 'a') =",x)
    print("address of 'x' (image of global 'a')",id(x))
    print()

    # modification of global variable 'a'
    globals()['a'] = 15


funct()
print("final value of global variable 'a' after funct() call:",a)
