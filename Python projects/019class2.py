class person:
    name=None
    age=None

    def Super_man_punch(self,x,y):
        self.name=x
        self.age=y
        print(self.name,"used a superman punch and it’s pure magic.")

a=person()
a.Super_man_punch(input("What's the name?"),int(input("What's the age?")))
#1
class army:
    def __init__(self,a,b,c):
        self.Archers=a
        self.footman=b
        self.Cavalier=c
        self.result=a*1+b*1.5+c*2
    def calculate_combat_power(self,m,n,x):
        self.Archers=m
        self.footman=n
        self.Cavalier=x
        return m*1+n*1.5+x*2
a1=army(12,11,2)
print(a1.calculate_combat_power(1,2,3))
