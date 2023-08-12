#for the user's currency and transactions
class Bank:
    def __init__(self):
        self.money_value = 0.0
    
class Transaction:
    def __init__(self, bank, sender, amount, datetime):
        self.bank = bank 
        self.sender = sender 
        self.amount = amount
        self.datetime = datetime 