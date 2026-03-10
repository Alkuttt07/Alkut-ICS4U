import random
class archers:
    def __init__(self):
        self.name=["Archers","",""]
        self.num=100
        self.unithp=5
        self.hp=self.num*self.unithp
        self.unitdamage=6

    def attack(self,target):
        print(f"""Before the attack, your selected army's number was {self.num}, the target's number was {target.num}.""")
        target.hp-=self.unitdamage*self.num
        bugfix(self,target)
        target.num=int(target.hp//target.unithp)
        print(f"""After the attack, your army's number is still the same and you caused {self.unitdamage*self.num} damage.
The target's number has become {target.num}.""")      

class footman:
    def __init__(self):
        self.name=["Footman","",""]
        self.num=100
        self.unithp=10
        self.hp=self.num*self.unithp
        self.unitdamage=5
    
    def attack(self,target):
        print(f"""Before the attack, your selected army's number was {self.num}, the target's number was {target.num}.""")
        target.hp-=self.unitdamage*self.num
        self.hp-=self.unitdamage*self.num*0.4
        bugfix(self,target)
        self.num=int(self.hp//self.unithp)
        target.num=int(target.hp//target.unithp)
        print(f"""After the attack, your army's number has become {self.num} and you caused {self.unitdamage*self.num} damage.
The target's number has become {target.num}.""")

class cavaliers:
    def __init__(self):
        self.name=["Cavaliers","",""]
        self.num=100
        self.unithp=6
        self.hp=self.num*self.unithp
        self.unitdamage=8
    
    def attack(self,target):
        if target.name[0]=="Spearmen":
            print(f"""Before the attack, your selected army's number was {self.num}, the target's number was {target.num}.""")
            target.hp-=self.unitdamage*self.num*0.5
            self.hp-=self.unitdamage*self.num*0.6
            bugfix(self,target)
            self.num=int(self.hp//self.unithp)
            target.num=int(target.hp//target.unithp)
            print(f"""This attack is weaker because the target is spearmen.
After the attack, your army's number has become {self.num} and you caused {self.unitdamage*self.num} damage.
The target's number has become {target.num}.""")
        else:
            print(f"""Before the attack, your selected army's number was {self.num}, the target's number was {target.num}.""")
            target.hp-=self.unitdamage*self.num    
            self.hp-=self.unitdamage*self.num*0.2
            bugfix(self,target)
            self.num=int(self.hp//self.unithp)
            target.num=int(target.hp//target.unithp)
            print(f"""After the attack, your army's number has become {self.num} and you caused {self.unitdamage*self.num} damage.
The target's number has become {target.num}.""")

class spearmen:
    def __init__(self):
        self.name=["Spearmen","",""]
        self.num=100
        self.unithp=20
        self.hp=self.num*self.unithp
        self.unitdamage=4.5

    def attack(self,target):
        if target.name[0]=="Cavaliers":
            print(f"""Before the attack, your selected army's number was {self.num}, the target's number was {target.num}.""")
            target.hp-=self.unitdamage*self.num*5
            self.hp-=self.unitdamage*self.num*0.2
            bugfix(self,target)
            self.num=int(self.hp//self.unithp)
            target.num=int(target.hp//target.unithp)
            print(f"""This attack is stronger because the target is cavaliers.
After the attack, your army's number has become {self.num} and you caused {self.unitdamage*self.num} damage.
The target's number has become {target.num}.""")

        else:
            print(f"""Before the attack, your selected army's number was {self.num}, the target's number was {target.num}.""")
            target.hp-=self.unitdamage*self.num
            self.hp-=self.unitdamage*self.num*0.2
            bugfix(self,target)
            self.num=int(self.hp//self.unithp)
            target.num=int(target.hp//target.unithp)
            print(f"""After the attack, your army's number has become {self.num} and you caused {self.unitdamage*self.num} damage.
The target's number has become {target.num}.""")

class mages:
    def __init__(self):
        self.name=["Mages","","(Unavailable)"]
        self.num=50
        self.unithp=8
        self.hp=self.num*self.unithp
        self.unitdamage=20
        self.magicstrength=100

    def attack(self,target):
        print(f"""Before the attack, your selected army's number was {self.num}, the target's number was {target.num}.""")
        target.hp-=self.unitdamage*self.num*(1+random.random())
        self.magicstrength-=100
        bugfix(self,target)
        target.num=int(target.hp//target.unithp)
        print(f"""After the attack, your army's number is still the same and you caused {self.unitdamage*self.num} damage.
The target's number has become {target.num}.
However, you have run out of your magicstrengh that takes 4 rounds to refresh.""")      

players=[[mages()],[mages()]]

def choose():
    for x in range(9):
        c=int(input(f"""Player 1, please choose your army No.{x+2}.
1.Archers    2.Footmen    3.Cavaliers    4.Spearmen     """))
        if c==1:
            players[0].append(archers())
        elif c==2:
            players[0].append(footman())
        elif c==3:
            players[0].append(cavaliers())
        elif c==4:
            players[0].append(spearmen())
        else:
            print("The value is invalid. Please restart the game.")
            exit()
    for y in range(9):
        c=int(input(f"""Player 2, please choose your army No.{y+2}.
1.Archers    2.Footmen    3.Cavaliers    4.Spearmen     """))
        if c==1:
            players[1].append(archers())
        elif c==2:
            players[1].append(footman())
        elif c==3:
            players[1].append(cavaliers())
        elif c==4:
            players[1].append(spearmen())
        else:
            print("The value is invalid. Please restart the game.")
            exit()

def mt(n):
    if players[n][0].name[1]!="Dead":
        if players[n][0].magicstrength<100:
            players[n][0].magicstrength+=25
            players[n][0].name[1]="(Unavailable)"
        else:
            players[n][0].name[1]=""

def bugfix(f1,f2):
        if f1.hp<0:
            f1.hp=0
        if f2.hp<0:
            f2.hp=0

def detectdeath(m):
    for x in players[m]:
        if x.hp<=0:
            x.name[1]="(Dead)"
            x.name[2]="(Dead)"

def targdetect(d,e,f):
    if players[d][f].name[0]=="Cavaliers":
        for x in range(10):
            if players[e][x].hp>0 and players[e][x].name[0]=="Archers":
                players[e][x].name[2]=""
    else:
        for y in range(10):
             if players[e][y].hp>0 and players[e][y].name[0]=="Archers":
                 players[e][y].name[2]="(Unavailable)"
    d1=[]    
    for z in range(9):
        if players[e][z+1].hp>0:
            d1.append(False)
    if all(d1)==True:
        players[e][0].name[2]=""
    d2=[]
    for p1 in range(9):
        if players[e][p1+1].hp>0 and players[e][p1+1].name[0]!="Archers":
            d2.append(False)
    if all(d2)==True:
        for p2 in range(9):
            if players[e][p2+1].name[0]=="Archers" and players[e][p2+1].hp>0:
                players[e][p2+1].name[2]=""

def select(b,c):
        print(f"""Player {b+1}, here are your armies.
Please select one as your attacking army.""")
        for i in range(10):
            print(f"{i+1}.{players[b][i].name[0]} {players[b][i].name[1]}")
        print("11.skip")
        while True:
            c1=int(input())
            if c1>=1 and c1!=11:
                if players[b][c1-1].name[1]=="(Unavailable)" or players[b][c1-1].name[1]=="(Dead)":
                    print("Please select an available army.")
                else:
                    targdetect(b,c,c1-1)
                    print(f"""Player {b+1}, your current number of the selected army is {players[b][c1-1].num}.
Here are the target's armies.
Please select one to attack.""")
                    for o in range(10):
                        print(f"{o+1}.{players[c][o].name[0]} {players[c][o].name[2]}")
                    while True:
                        c2=int(input())
                        if players[c][c2-1].name[2]=="(Unavailable)" or players[c][c2-1].name[2]=="(Dead)":
                            print("Please select an available army.")
                        else:
                            players[b][c1-1].attack(players[c][c2-1])
                            return
            elif c1==11:
                return

def randevent():
    r=random.random()
    rr=random.randint(1,9)
    if 0<=r<0.2 and players[0][0].magicstrength<=50:
        print("\033[31mPlayer 1's mage has been blessed, gained 50 magic strength.\033[0m")
        players[0][0].magicstrength+=50
    elif 0.2<=r<0.4 and players[1][0].magicstrength<=50:
        print("\033[31mPlayer 2's mage has been blessed, gained 50 magic strength.\033[0m")
        players[1][0].magicstrength+=50
    elif 0.4<=r<0.6 and players[0][rr].name[1]!="(Dead)":
        print(f"\033[31mArmy No.{rr+1} of plyer 1 is hit by a meteorite. No people survived.\033[0m")
        players[0][rr].hp=0
        players[0][rr].num=0
        players[0][rr].name[1]="(Dead)"
        players[0][rr].name[2]="(Dead)"
    elif 0.6<=r<0.8 and players[1][rr].name[1]!="(Dead)":
        print(f"\033[31mArmy No.{rr+1} of plyer 2 is hit by a meteorite. No people survived.\033[0m")
        players[1][rr].hp=0
        players[1][rr].num=0
        players[1][rr].name[1]="(Dead)"
        players[1][rr].name[2]="(Dead)"
    else:
        print("\033[31mNo special events happened.\033[0m")
def main():
    print("""The game get started. 
There are 4 possible troops for an army: Archers, Spearman, Cavaliers, Footman.
Also, there is another troop that is called Mages that is defaulted to be the Army No.1 for each player.
The player's armies will take turns to attack. When an army attacks, players should select which squadron they use and which enemy squadron they wish to attack.""")
    choose()
    while True:
        select(0,1)
        mt(0)
        detectdeath(1)
        detectdeath(0)
        select(1,0)
        mt(1)
        detectdeath(0)
        detectdeath(1)
        randevent()
        if players[0][0].hp<=0:
            print("\033[33mPlayer 2 is the winner. Thank you for playing.\033[0m")
            #only mages die == every army die == game over (because we can attack mages only after the other armis die)
            break
        elif players[1][0].hp<=0:
            print("\033[33mPlayer 1 is the winner. Thank you for playing.\033[0m")
            #only mages die == every army die == game over (because we can attack mages only after the other armis die)
            break
main()