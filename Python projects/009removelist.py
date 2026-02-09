import random
a=[random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
del a[2]
a.append(12)
a.insert(2,random.randint(1,20))
b=int(input("integer"))
if b!=0:
    a.append(b)
    print(a)
else:
    print("program ending.")