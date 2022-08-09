s = "himu"
n = 78
l = [3,4,5,6,7,"himu",45.8,6+7j,[3,4,5,6,7]]
t = (3,4,5,6,7)
d = {"y" : "fsdfsd",5 :"rerteedre",n:{"name" : "himu" ,"mail_id" : "himu@gmail.com"}}
print(s[-1])
print(s[1])
print(s[2])
print(s[0:100])
print(d)
print(iter(d))
for i in d.keys():
    print(d[i])
for i in d.items():
    print(i)
for i in d.keys():
    if type(d[i]) == dict:
        for j in d[i].keys():
            print(d[i][j])
for i in d.keys():
    if type(d[i]) == dict:
        for j in d[i].items():
            print(j)
d = {"key1" : "himu" , "key1" : [1,2,3,4,5,6,7,8]}
print(d["key1"])
d["key2"] =(2,3,4,5,6)
print(d)
d["key1"] = "balodi"
print(d)
t = (2,4,5,67,68)
print(t[0])
print(t[-1])

l = [2,33,54,65,6,]
print(l)
l[0] = 223
print(l)
t = (2,3,4,5,5,6)
l2 = list(t)
print(l2)
l2[0] = 223
print(l2)
print(tuple(l2))
print(list(range(10)))
for i in range(10):
    print(i)
r = iter(range(10))
print(next(r))
print(next(r))
for i in range(10):
    print(i**2)
def fib(n):
    a=0
    b=1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
fib(10)

##
number=int(input("Enter a number:"))
def fibonacci(number):
    fib = []
    count = 0
    for i in range(number):
        if i == 0:
            fib.append(i)
        elif i == 1:
            fib.append(i)
        else:
            fib.append(fib[-1]+fib[-2])
    return fib
fibonacci(number)
##
lst=[]

def fibo(n):
    a,b=1,1
    for i in range(n):
        yield a,i
        a,b=b,a+b

for c,i in fibo(10):
    lst.append(c)

##
for i in fibo(4):
    print(i)
