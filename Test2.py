# Inheritance multilevel.
class bank :
    def transaction(self):
        print("total transication value")
    def account_opening(self):
        print("this is show you your account open")
    def deposite(self):
        print("this will show your deposit amount")
    def test(self):
        print("this is test method from bank class")

class HDFC_bank :
    def hdfc_to_icici(self):
        print("this will show you all the transication happend to icici through hdfc")
    def test(self):
        print("this is method from hdfc bank")

class ineuron_bank:
    def account_status_icici(self):
        print("print a account status in icici")

class icici(HDFC_bank,bank,ineuron_bank):
    pass

i =icici()
i.hdfc_to_icici()
i.account_opening()
i.transaction()
i.deposite()
i.test()
i.account_status_icici()