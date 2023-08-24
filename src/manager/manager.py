from skill_tree import SkillTree
from bank import Bank, Transaction

class Manager:
    def __init__(self, name):
        self.skill_tree = SkillTree("owner")
        self.name = name
        self.bank = Bank()
        self.businesses = []

    def print_name(self):
        print(self.name)

    def start_business(self, business, date):
        if self.bank.money_value < business.upfront_cost:
            return "Not enough money"
        self.businesses.append(business)
        business.owner = self

        #issue the transaction
        trans = Transaction(self.bank, self, business.upfront_cost, date)


    
