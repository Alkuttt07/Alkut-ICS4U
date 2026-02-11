a=[4,7,1,3,9]
b=0
for x in a:
    b+=x
print(b)
#1
import random
c=[12,5,8,19,3]
d=random.choice(c)
for y in c:
    if y<d:
        d=y
print(d)
#2
e=[9,8,7,6,5]
f=[]
for z in range(5):
    f.append(e[-(z+1)])
print(f)
#3
g=[2,5,6,2,8,2,3]
h=0
for m in g:
    if m==2:
        h+=1
print(h)
#4
i=[4,6,4,7,6,8,4]
for n in i:
    for k in i:
        if i.index(n)!=i.index(k) and k==n:
            i.pop(i.index(k))
print(i)
#5