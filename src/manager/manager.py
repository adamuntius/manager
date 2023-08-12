from skill_tree import SkillTree
from bank import Bank

class Manager:
    def __init__(self, name):
        self.skill_tree = SkillTree("owner")
        self.name = name
        self.bank = Bank()
    def print_name(self):
        print(self.name)
