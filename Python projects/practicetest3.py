#1
class student:
    def __init__(self,a,b,e):
        self.name=a
        self.id=b
        self.coursesandgrades=e
    def adding(self,c,d):
        self.coursesandgrades.update({c:d})
d1={}
class karate_kids(student):
    def __init__(self, a, b,e):
        super().__init__(a, b,e)
    def fight(self):
        print("lalala")
    def stor(self):
        d1.update({self.name:[self.id,self.coursesandgrades]})
    def view(self):
        print(d1[self.name])

p1=karate_kids("alkut",123332,{"ENG4U":93})
p1.adding("ISC4U",98)
p1.adding("MCV4U",100)
p1.stor()
p1.view()

#2
import practicetest3usefulfunction
def f1():
    a=input("hear or tell")
    if a==0:
        l1=input("list")
        practicetest3usefulfunction.telljokes(l1)
    elif a==1:
        practicetest3usefulfunction.writejokes()

f1()