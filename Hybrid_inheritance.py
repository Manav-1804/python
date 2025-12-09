class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print(" A : ",self.a)

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print(" B : ",self.b)

class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print(" C : ",self.c)

class D(B,C):
    def getD(self,d):
        self.d=d
    def putD(self):
        print(" D : ",self.d)

b1=D()

b1.getA(10)
b1.getB(20)
b1.getC(30)
b1.getD(40)
b1.putA()
b1.putB()
b1.putC()
b1.putD()

