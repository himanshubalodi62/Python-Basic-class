from utill1 import person2

obj = person2("himanshu " , "balodi" , 345345)
print(obj.yob1)

class person1 :
    def __init__(self , name ,surname , yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

himu = person1("himanshu" , "balodi" , 1990)
print(himu._name1)
print(himu._person1__surname1)
