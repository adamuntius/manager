class Skill:
    def __init__(self, name, description, activation_function, deactivation_function, cost_conditions):
        self.name = name
        self.description = description
        self.activation_function = activation_function
        self.deactivation_function = deactivation_function
        self.cost_conditions = cost_conditions
    def activate():
        activation_function()
    def deactivate():
        deactivation_function()

#A Perk is like a skill but has no cost conditions
class Perk(Skill):
    def __init__(self, name, description, activation_function, deactivation_function, cost_conditions):
        if len(cost_conditions) != 0:
            raise Exception("A perk should have no cost conditions")
        Skill.__init__(self, name, description, activation_function, deactivation_function, cost_conditions)
    pass

class SkillTree:

    def initialize_skill_list(self):
        new_skill_list = []
        generalist = Skill("generalist", "Revenue from all businesses increases by 1%.", None, None, [])
        new_skill_list.append(generalist)
        tech_specialist = Skill("tech specialist", "Revenue from all tech businesses increases by 2%", None, None, [])
        new_skill_list.append(tech_specialist)
        real_estate_specialist = Skill("real estate specialist", "Revenue from all real estate businesses increases by 2%", None, None, [])
        new_skill_list.append(real_estate_specialist)
        entrepreneur = Skill("entrepreneur", "Open new businesses 5% faster.", None, None, [])
        new_skill_list.append(entrepreneur)
        return new_skill_list
    
    def print_skill_list(self):
        for skill in self.skill_list:
            print(skill.description)

    def __init__(self, owner_type):
        if owner_type != "business" and owner_type != "owner":
            raise Exception("Invalid owner type for skill tree")
        self.owner_type = owner_type
        self.skill_list = self.initialize_skill_list()