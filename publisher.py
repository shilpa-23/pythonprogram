class Publisher():
    def __init__(self,name):
       self.name=name
    def display(self):
        print(self.name)

class Book(Publisher):
        def __init__(self,name,title,author):
            self.title=title
            self.author=author
            super().__init__(name)

        def display(self):
            print(self.name, self.title, self.author)

class python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        self.price= price
        self.noofpages= no_of_pages
        super().__init__(name, title, author)

    def display(self):
        print(self.name, self.title, self.author, self.price, self.noofpages)

a=input("Enter The Name Of Author:")
na=input("enter name of publisher:")
ti=input("enter the title:")
p=int(input("enter the price :"))
pg=int(input("enter no of pages:"))

t= Publisher(na)
b = Book(na,ti,a)
p = python(na, ti, a, p, pg)
p.display()
b.display()
t.display()