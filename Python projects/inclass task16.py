class Spells:
    def __init__(self,a,b,c,d):
        self.name=a
        self.MP_cost=b
        self.damage=c
        self.cooldown=d

class Mages:
    def __init__(self,e,f,g,h,i,j):
        self.name=e
        self.Hp=f
        self.MP=g
        self.Spell1=h
        self.Spell2=i
        self.Spell3=j
        
    def casting_Spells(self):
        k=int(input("Which spell to cast? 1,2,3?"))
        
        if k==1:
            print(self.Spell1.name)
            print(self.Spell1.damage)
            self.MP-=self.Spell1.MP_cost
            print(self.MP)
        elif k==2:
            print(self.Spell2.name)
            print(self.Spell2.damage)
            self.MP-=self.Spell2.MP_cost
            print(self.MP)
        elif k==3:
            print(self.Spell3.name)
            print(self.Spell3.damage)
            self.MP-=self.Spell3.MP_cost
            print(self.MP)
        else:
            print("Casting failure.")

s1= Spells("lalalala",20,40,4)
s2= Spells("babababa",5,15,1)
s3= Spells("papapapa",50,66,15)

Alkut = Mages("A",100,100,s1,s2,s3)
Alkut.casting_Spells()