class Rectangle:
    def __init__(self):
        self.length=int(input("Enter the length :"))
        self.breadth=int(input("Enter the breadth :"))
    def area(self):
        self.a=self.length*self.breadth
        print("Area of Rectangle :",self.a)
        return self.a
    def perimeter(self):
        self.p=2*(self.length+self.breadth)
        print("Perimeter of Rectangle :",self.p,"\n")

x=Rectangle()
print("\n__Rectangle 1__")
a1=x.area()
x.perimeter()

y=Rectangle()
print("\n__Rectangle 2__")
b1=y.area()
y.perimeter()

if a1>b1:
        print("Rectangle 1 is bigger.")
elif a1==b1:
      print("Both rectangles are of same area")
else:
    print("Rectangle 2 is bigger.")

