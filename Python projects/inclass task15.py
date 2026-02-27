class quadratic_relationship:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def intercepts(self):
        if self.b**2-4*self.a*self.c<0:
            return f"There is no x intercepts, but y intercept is (0,{self.c})."
        elif self.b**2-4*self.a*self.c==0:
            return f"x intercept is ({-self.b/(2*self.a)},0), and y intercept is (0,{self.c})."
        else:
            return f"x intercepts are ({(-self.b+(self.b**2-4*self.a*self.c)**0.5)/(2*self.a)},0) and ({(-self.b-(self.b**2-4*self.a*self.c)**0.5)/(2*self.a)},0), and y intercept is (0,{self.c})."
x=quadratic_relationship(int(input("What's the a")),int(input("What's the b")),int(input("What's the c")))
print(x.intercepts())