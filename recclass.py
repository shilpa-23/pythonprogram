class rect:
    def __init__(self, a,b):
        self.length = a
        self.breadth=b
    def area(self):
        return self.length*self.breadth

    def __lt__(self, o):
        if (self.area() < o.area()):
            return True
        else:
            return False

h1=int(input("enter hight of  rectangle 1:"))
b1=int(input("enter breadth of  rectangle 1:"))
h2=int(input("enter hight of  rectangle 2:"))
b2=int(input("enter breadth of  rectangle 2:"))


rect1 = rect(h1,b1)
rect2=rect(h2,b2)
if (rect1 <rect2):
    print("rectangle 1 is lessthan than rectangle 2")
else:
    print("rectangle 2 is lessthan than rectangle 1")
