def sum(a=10,b=20):
    print(a)
print(sum())
##
def sum(a=10,b=20):
    return a
print(sum()+60)
def sum(a=10,b=[23,33,3,4]):
    return a,b
print(sum())
m , n = sum()
print(m)
print(n)
_,_ = sum()
print(_)
print(_)
def test(a,b,c,d,g,h):
    return a
def test(*args):
    return args
print(test(3,4,5,6,7))
print((test(3,4,5,6,7),[44,5,6,7,6,4],(34,44,5,676)))
def test1(**kwargs):
    return kwargs
print(test1(a=23,b=56,himu=45,balodi=34))
def test1(**himu):
    return himu.keys()
print(test1(a=23,b=56,himu=45,balodi=34))
def test1(**himu):
    return himu.values()
print(test1(a=23,b=56,himu=45,balodi=34))
def test1(**himu):
    return himu.items()
print(test1(a=23,b=56,himu=45,balodi=34))
def test(a,b):
    return a+b
print(test (23,45))
l = lambda a,b : a+b
print(l(23,45))
def test(a,b):
    """this is my function to  add two variable
    sfdfs
    sfsfs
    sdfs"""
    return a + b
help(test)

l = [2,3,4,5,5,6,]
l1=[]
for i in l:
    l1.append(i*2)
print(l1)
print([i+2 for i in l])
print({i:i**2 for i in l})
d = { }
for i in l:
    d[i] = i**2
print(d)
class test1:
    def __int__(a,b,c,d):
        pass





