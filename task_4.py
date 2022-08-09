class parent:
    def test(self, a,b):
        print("this is my parent class method")
class parent1:
    def test(self ):
        print("this is my second class method")
class child(parent,parent1):
    def test_child(self):
        print("this is my child class method")
c = child()
print(c.test(3,4))


class c1:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return "this is my c1 class %s %s %d" %(self.a,self.b,self.c)

c__obj = c1("himu" "balodi" , 5)
print(c1__obj)
class c2 :
    def __init__(self,x,y):
        self.x= x
        self.y = y
    def __str__(self):
        return "this is a return c2 class %s %f" %(self.x,self.y)
c2__obj1 = c2("himanshu",56)
print(c2__obj1)