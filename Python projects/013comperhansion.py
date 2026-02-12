a=[1,2,3,4,5,6,7,8,9,0]
b=[]
for x in a:
    if x%2==0:
        b.append(x)
print(b)
#1
c=[y for y in a if y%2==0]
print(c)
#2
name=["ascjihaheifhefwhuifw","bbbbb","ssaa"]
champion3=[]
for z in name:
    if "a" in z:
        champion3.append(z)
print(champion3)
#3
d=[]
for n in range(10):
    if n<5:
        d.append(n)
print(d)
#4
e=[1,2,3,4,5,6,7,8,9,10]
f=[]
for m in e:
    if m%2==0:
        f.append("two")
    elif m%3==0:
        f.append("three")
    else:
        f.append("not two or three")
print(f)
#5