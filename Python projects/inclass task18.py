l1=[]
class info:
    name=None
    age=None
    gender=None
    hobby=None

    def coll(self):
        self.name=input("What's the name?")
        self.age=int(input("What's the age?"))
        self.gender=input("What's the gender")
        self.hobby=input("What's the hobby?")
    
    def prin(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.hobby)
    
    def lis(self):
        l1.append([self.name,self.age,self.gender,self.hobby])

def main():
    p1=info()
    p1.coll()
    p1.prin()
    p1.lis()
    print(l1)

main()