a=[[],[],[0,1]]
for x in range(10):
    a[0].append(2*x)
    a[1].append(1+2*x)
for y in range(8):
    a[2].append(a[2][-1]+a[2][-2])
while True:
    if input("do you want a factorial number, if so answer yes") == "yes":
        b=a[int(input("1.even 2.odd 3.fibonacci"))-1]
        c=int(b[int(input("which order"))-1])
        for z in range(c):
            c*=(c-z)
        print(c)
    else:
        break