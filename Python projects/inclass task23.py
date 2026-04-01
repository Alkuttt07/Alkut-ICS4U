class mammals:
    def __init__(self,a,b):
        a=a
        b=b
    def attack(self):
        print("sakdsjdak")

class tigers(mammals):
    def __init__(self, a, b):
        super().__init__(a, b)
    def attack(self):
        print("HAhaha")

class human(mammals):
    def __init__(self, a, b):
        super().__init__(a, b)
    def attack(self):
        print("163726313127")

p1=mammals(2,4)
p2=tigers(1,3)
p3=human(4,2)
p1.attack()
p2.attack()
p3.attack()