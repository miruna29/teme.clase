# This is a sample Python script.
#tema clase - fractii

from math import gcd

class Rational:
    def __init__ (self,a=None,b=None):
        self.a=a
        self.b=b
    def __add__ (self,s):
        return self.a*s.b+self.b*s.a,self.b*s.b
    def __mul__(self,s):
        n=Rational(self.a*s.a,self.b*s.b)
        return n.simplify()
    def __str__(self):
        return '%i/%i'%(self.a,self.b)

if __name__ == "__main__":
    while True:
        a=int(input('a='))
        b=int(input('b='))
        r1=Rational(a,b)
        c=int(input('c='))
        d=int(input('d='))
        r2=Rational(c,d)
        x=r1+r2
        print(x)


