import random
def f1():
    return random.randint(1,20)
print(f1())

def f2(n):
    l1=[random.randint(1,20) for x in range(n)]
    l2=[y for y in l1 if y>5]
    print(l2)
f2(int(input("How many numbers you want?")))