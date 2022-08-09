class ineuron :
    def student(self):
        print("the detail of all the students ")

    def achivers(self):
        print("the list of all the achivers")

    def hall_of_fame(self):
        print("everyone form hall of fame")

class ineuron_vision(ineuron):  ##method overiding.

    def student(self):
        print("these are the filters student list")

iv = ineuron_vision()
iv.student()