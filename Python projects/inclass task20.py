class student():
    def __init__(self,a,b):
        self.age=a
        self.gender=b
d1={
    "Alkut":student(18,"m"),
    "Leon":student(49,"m"),
    "Ada":student(51,'f'),
    "Niko":student(30,"m"),
    "CJ":student(31,"m"),
}
for x in d1:
    print(d1[x].age)
    print(d1[x].gender)
