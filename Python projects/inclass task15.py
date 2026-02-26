class quadratic_relationship:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.yintercept=c
    def xintercepts(self):
        if self.b**2-4*self.a*self.c<0:
            return "There is no x intercepts."
        elif self.b**2-4*self.a*self.c==0:
            return -self.b/(2*self.a)
        else:
            return [(-self.b+(self.b**2-4*self.a*self.c)**0.5)/(2*self.a),(-self.b-(self.b**2-4*self.a*self.c)**0.5)/(2*self.a)]