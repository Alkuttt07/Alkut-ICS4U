print(f"Hello,{input("What's your name? ")}!")
#1
print("".join([x for x in "...I love high school..." if x!="."]))
#2
print(sum([y for y in range(1,101) if y%2==0]))
#3
fruits = ["Apple", "Pear", "Orange", "Banana", "Mango"]
l1=[z for z in fruits if "e" in z]
print(l1)
#4
l2=[x for x in range(1,101) if x%2==0]
print(l2)
#5
a="I am R2D2, hahaha."
b=[x for x in a]
b.reverse()
print("".join(b))
#6
l3=[[],[],[],[],[]]
for x in range(5):
    l3[x].append(input(f'{x+1}.Name? '))
    l3[x].append(input(f'{x+1}.age? '))
    l3[x].append(input(f'{x+1}.gender? '))
print("name    age    gender")
for y in l3:
    print(y)
#7
l4=[x for x in range(2,101) if all([x%y for y in range(2,x)])==True]
print(l4)
#8
