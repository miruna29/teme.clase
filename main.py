#exercitii clase

from math import gcd
class fractie():
    def __init__ (self,a,b):
        self.a=a
        self.b=b
    def add (self,s):
        return fractie(self.a*s.b+self.b*s.a,self.b*s.b).simplify()
    def sub (self,s):
        return fractie(self.a*s.b-self.b*s.a,self.b*s.b).simplify()
    def mul(self,s):
        n=fractie(self.a*s.a,self.b*s.b)
        return n.simplify()
    def simplify(self):
        d=gcd(self.a,self.b)
        self.a/=d
        self.b/=d
    def inv(self):
        return (self.a/self.b)**-1
    def to_string(self):
        return '%i/%i'%(self.a,self.b) #se inlocuieste in loc de %i valoarea din paranteza

def main():
    while True:
        a = int(input('a='))
        b = int(input('b='))
        fractie1 = fractie(a, b)
        c = int(input('c='))
        d = int(input('d='))
        fractie2 = fractie(c, d)
        res = fractie(fractie1,fractie2)
        res = fractie1.add(fractie2)
        print(res.to_string())

main()

