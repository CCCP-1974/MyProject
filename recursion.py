import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 1

def toto():
    global i
    print('Hello', i)
    i += 1
    toto()

toto()