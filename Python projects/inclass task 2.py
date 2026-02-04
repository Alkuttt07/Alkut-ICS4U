a = int(input("Please show your first integer."))
b = int(input("Please show your second integer."))
c = int(input("Please show your third integer."))
e = 0
f = 0
if a>=b and a>=c:
    d=a
elif b>=a and b>=c:
    d=b
elif c>=a and c>=b:
    d=c
if a%2==0:
    e+=1
else:
    f+=1
if b%2==0:
    e+=1
else:
    f+=1
if c%2==0:
    e+=1
else:
    f+=1
if e>1:
    g="are"
    j="s."
else:
    g="is"
    j= "."
if f>1:
    h="are"
    k="s."
else:
    h="is"
    k= "."
print(f"""The biggest integer is {d}.
The average of the integers is {(a+b+c)/3}.
There {g} {e} even integer{j}
There {h} {f} odd integer{k}""")