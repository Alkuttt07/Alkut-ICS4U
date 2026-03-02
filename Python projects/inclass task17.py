class super_heroes():
    def __init__(self,a1,a2,a3,a4,a5,a6):
        self.name=a1
        self.strength=a2
        self.speed=a3
        self.health=a4
        self.intelligence=a5
        self.abilities=a6
    
    def physical_attack(self):
        if self.name==p1.name:
            p2.health-=self.strength
            print(p2.health)
        elif self.name==p2.name:
            p1.health-=self.strength
            print(p1.health)
    
    def casting_spell(self,c,d):
        if self.name==p1.name:
            if c==0:
                p2.health-=self.abilities[int(d)-1].damage
                print(p2.health)
            elif c==1:
                self.health+=self.abilities[int(d)-1].selfheal
                print(p1.health)
        elif self.name==p2.name:
            if c==0:
                p1.health-=self.abilities[int(d)-1].damage
                print(p1.health)
            elif c==1:
                self.health+=self.abilities[int(d)-1].selfheal
                print(p2.health)

class spells:
    def __init__(self,b1,b2,b3):
        self.name=b1
        self.damage=b2
        self.selfheal=b3

s1=spells("w",20,10)
s2=spells("q",40,23)
p1=super_heroes("aaa",15,6,100,120,[s1,s2])
p2=super_heroes("bbb",10,5,200,100,[s1,s2])

p1.physical_attack()
p2.physical_attack()
p1.casting_spell(0,1)
p1.casting_spell(0,2)
p2.casting_spell(1,1)
p2.casting_spell(1,2)