class weapons:
    def __init__(self,damage,cooldown,weapon_type):
        self.damage=damage
        self.cooldown=cooldown
        self.weapon_type=weapon_type
    def attack(self):
        global target
        target=input("What's your target?")
        print(self.damage)

class energy_weapon(weapons):
    def __init__(self,damage,cooldown,weapon_type):
        super().__init__(damage,cooldown,weapon_type)
    
    def radiation(self):
        print("Ouch, everyone is suffering from radioactive substance.")

class kinetic_weapon(weapons):
    def __init__(self,damage,cooldown,weapon_type,ammunition_counts):
        super().__init__(damage,cooldown,weapon_type)
        self.ammunition_counts=ammunition_counts

p1=energy_weapon("a1",11,"b1")
p2=energy_weapon("a2",1,"b2")
p3=energy_weapon("a3",2,"b3")
p4=kinetic_weapon("a4",5,"b4",20)
p5=kinetic_weapon("a5",3,"b5",15)
p6=kinetic_weapon("a6",2,"b6",30)

d1={"player1":p1,
    "player2":p2,
    "player3":p3,
    "player4":p4,
    "player5":p5,
    "player6":p6
    }