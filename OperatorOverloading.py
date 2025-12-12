class Point:
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y

    def __str__(self):
        print("str called")
        return"({0},{1})".format(self.x,self.y)

    def __add__(self,obj):
        print("add called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)

    def __sub__(self, obj):
        print("sub called")
        x = self.x - obj.x
        y = self.y - obj.y
        return Point(x, y)

    def __mul__(self, obj):
        print("mul called")
        x = self.x * obj.x
        y = self.y * obj.y
        return Point(x, y)

    
    

p1=Point(10,20)
print(p1)
p2=Point(30,40)
print(p2)
print("Addition Of 2 Objects : ",p1+p2)
print("Subtraction of 2 Objects :", p1 - p2)
print("Multiplication of 2 Objcets:", p1 * p2)

