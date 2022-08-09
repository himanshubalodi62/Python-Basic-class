#multiple inheritance:
class bank :
    def transaction(self):
        print("total transication value")
    def account_opening(self):
        print("this is show you your account open")
    def deposite(self):
        print("this will show your deposit amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transication happend to icici through hdfc")

class icici(HDFC_bank):
    pass

i=icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()