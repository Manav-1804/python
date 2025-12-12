from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(r):
        pass

    def show(self):
        print("Show From RBI")

class SBI(RBI):


    def roi(self,r):
        print("Rate of Interest Given By SBI Is : ",r)

class HDFC(RBI):


    def roi(self,r):
        print("Rate of Interest Given By HDFC Is : ",r)

s1=SBI()

s1.show()
s1.roi(6.7)
print("-"*80)
h1=HDFC()
h1.roi(7.6)
