def loadjokes():
    with open("practicetest2text.txt") as tx1:
        print(tx1.readlines)
import random
def telljokes(a):
    with open("practicetest2text.txt") as tx1:
        l1=tx1.readlines
        print(l1[random.choice(a)])
def writejokes():
    with open("practicetest2text.txt","a") as tx1:
        tx1.write(f"\n{input("joke")}")

