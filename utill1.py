class person2:
    def __init__(self , name ,surname , yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

himu = person2("himanshu" , "balodi" , 1990)
print(himu._name1)
print(himu._person2__surname1)
