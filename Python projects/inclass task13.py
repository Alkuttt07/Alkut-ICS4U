#1
def f1(a):
    l1=[0,1]
    if a>2: 
        for x in range(a-2):
            l1.append(l1[-1]+l1[-2])
        return l1[-1]
    elif a==2:
        return 1
    elif a==1:
        return 0
print(f1(int(input("Please input the position."))))
#2
def f2(b,c,d,e):
    l2=[b,c,d,e]
    l2.sort()
    return l2
print(f2(float(input("first number")),float(input("second number")),float(input("third number")),float(input("fourth number"))))