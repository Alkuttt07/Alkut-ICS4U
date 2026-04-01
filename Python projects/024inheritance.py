class people:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
    def learn(self):
        pass
    def walk(self):
        pass
    def eat(self):
        pass

class programmer(people):
    def __init__(self,name,designation,companyname):
        super().__init__(name,designation)
        self.companyname=companyname
    def coding(self):
        pass
    
class singer(people):
    def __init__(self,name,designation,bandname):
        super().__init__(name,designation)
        self.bandname=bandname
    def singing(self):
        pass
    def playguitar(self):
        pass

p1=singer("alkut","0101010","Bell High School")
p1.playguitar()