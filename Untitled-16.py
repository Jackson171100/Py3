class replaceable:
    def __init__(self,name,debt,no_life,soon_to_be_unenployed):
        self.name=name
        self.debt=debt
        self.no_life=no_life
        self.soon_to_be_unenployed=soon_to_be_unenployed
    def add_debt(self,more_debt):
        self.debt+=more_debt
    def money_you_have_none_aka_gen_z(self):
        return self.debt
person1=replaceable("Joe",1000,True,True)
print(person1.name)
person1.add_debt(1200)
print(person1.debt)
print(person1.money_you_have_none_aka_gen_z())
def add_by_step()