class Person:

    def __init__(self,name,surname,emailid,year_of_birth):
        self.name1 = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_var = Person("himu" ,"balodi" , "himu@gmail.com" ,1995)
himanshu = Person("himanshu" ,"kumar","himanshu@gmail.com",4545)
print(anuj_var.name1)
print(himanshu.name1)
print(type(himanshu))