from skill_tree import SkillTree

class Manager:
    def __init__(self, name):
        self.skill_tree = SkillTree("owner")
        self.name = name
    def print_name(self):
        print(self.name)
