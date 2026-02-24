import random
def f1():
    return random.randint(1,20)
print(f1())

def f2(n):
    l1=[]
    for x in range(n):
        x = random.randint(1,20)
        if x > 5:
            l1.append(x)
