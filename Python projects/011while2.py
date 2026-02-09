a=0
b=[0,1]
while a<18:
    a+=1
    b.append(b[-1]+b[-2])
print(b)