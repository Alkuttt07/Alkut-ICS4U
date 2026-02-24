class people:
    name=None
    age=None
    gender=None
    height=None

p1=[people(),people(),people()]
for x in range(3):
    p1[x].name=input("What's the name?")
    p1[x].age=int(input("What is the age?"))
    p1[x].gender=input("What's the gender?")
    p1[x].height=int(input("What's the height?"))