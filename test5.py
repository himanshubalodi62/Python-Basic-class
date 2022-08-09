class person :

    def age(self,current_year ,year_of_birth):
        return current_year - year_of_birth
    def email_id_input(self,emai_id_):
        print("take and mail id from a person and print it",emai_id_)
    def ask_name(self):
        name = input("tell me your name")
        return name
    def ask_dob(self):
        dob = input("tell me your date of birth")
        return dob

himu = person()
sudh = person()
krish = person()
hitesh = person()
himu.email_id_input("sudhanshu@ineron.ai")
print(himu.ask_name())

print(hitesh.ask_dob())
