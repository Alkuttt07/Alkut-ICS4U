#1
def f1(a,b):
    if a%2==0 and b%2==0:
        return 1
    else:
        return 0
print(f1(int(input("First number")),int(input("second number"))))
#2
def f2(c):
    return [x**2 for x in range(c+1)]
print(f2(int(input("power base"))))
#3
l1=[1,4,3,4,5,4,3,2,4,7,9,4]
def f3(l1):
    return [x for x in l1 if x%2==0]
print(f3(l1))
#4
def f4(d):
    l2=[0,1]
    if d>2:
        for x in range(d-2):
            l2.append(l2[-1]+l2[-2])
        return l2[-1]
    elif d==2:
        return 1
    elif d==1:
        return 0
print(f4(int(input("fibonacci sequence"))))
#5
def f5(e,f,g,h):
    l3=[e,f,g,h]
    l3.sort()
    return l3
print(f5(float(input("first number")),float(input("second number")),float(input("third number")),float(input("fourth number"))))
#6
class Transformers:
    faction=None
    name=None
l4=[Transformers(),Transformers(),Transformers(),Transformers(),Transformers()]
l5=["Megatron","Optimus Prime","Starscream","Arcee","Grimlock"]
l6=[0,1,1,1,0]
for x in range(5):
    l4[x].name=l5[x]
    l4[x].faction=l6[x]
for y in range(5):
    print(l4[y].name)
def Autobots_attack(l4):
    return [l4[z].name for z in range(5) if l4[z].faction==1]
print(Autobots_attack(l4))
#7
class countries:
    name=None
    population=None
l7=[]
while True:
    n=int(input("Do you wish to add a country?"))
    if n==2:
        break
    if n==1:
        l7.append(countries())
        l7[-1].name=input("name")
        l7[-1].population=input("population")
