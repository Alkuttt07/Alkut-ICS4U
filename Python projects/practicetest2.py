#1
class person:
    def __init__(self,a,b):
        self.name=a
        self.age=int(b)

    def greet(self):
        print(f"Hello, I am {self.name}, I am {self.age} years old.")

l1=[person("Alkut",18),person("Leon",28),person("Ada",31),person("Niko",30)]

l1[2].greet()

#2
def linear(a,b):
    return [b,-b/a]

def quadratic(a,b,c):
    if b**2-4*a*c<0:
        return [c,None]
    elif b**2-4*a*c==0:
        return [c,-b/(2*a)]
    elif b**2-4*a*c>0:
        return [c,[(-b+(b**2-4*a*c)**0.5)/(2*a),(-b-(b**2-4*a*c)**0.5)/(2*a)]]
    
def sphere(x):
    return [4*3.14*(x**2),4*3.14*(x**3)/3]

def cuboid(x,y,z):
    return [x*y*z,2*(x*y+x*z+y*z)]

def main():
    l2=[linear(int(input("a?")),int(input("b?"))),
    quadratic(int(input("a?")),int(input("b?")),int(input("c?"))),
    sphere(int(input("x?"))),
    cuboid(int(input("x?")),int(input("y?")),int(input("z?")))]
    print(f"""
linear: y intercept is {l2[0][0]} and x intercept is {l2[0][1]}
quadratic: y intercept is {l2[1][0]} and x intercept is/are {l2[1][1]}
sphere: area is {l2[2][0]} and volume is {l2[2][1]}
cuboid: area is {l2[3][1]} and volume is {l2[3][0]}
""")

main()

#3
with open("practicetest2text.txt") as tx1:
    ll1="".join(tx1.readlines())
ll2=[ll1[x] for x in range(len(ll1)) if x%2==0]
ll1=[z for z in ll1]
with open("practicetest2text.txt","w") as tx2:
    for y in range(len(ll1)):
        if y%2==0:
            ll1[y]="a"
    tx2.write(f"{"".join(ll1)} \n {"".join(ll2)}")
with open("practicetest2text.txt") as tx3:
    print(tx3.readlines())

for a in range(len(ll2)):
    ll1[a*2]=ll2[a]

with open("practicetest2text.txt","w") as tx4:
    tx4.write("".join(ll1))

with open("practicetest2text.txt") as tx5:
    print(tx5.readlines())