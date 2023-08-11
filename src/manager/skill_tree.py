class SkillTree:
    
    
    class Skill:
        def __init__(self, name, description, activation_function, deactivation_function):
            self.name = name
            self.description = description
            self.activation_function = activation_function
            self.deactivation_function = deactivation_function
        def activate():
            activation_function()
        def deactivate():
            deactivation_function()
            

    def initialize_skill_list(self):
        new_skill_list = []
        generalist = self.Skill("generalist", "Revenue from all businesses increases by 1%.", None, None)
        new_skill_list.append(generalist)
        tech_specialist = self.Skill("tech specialist", "Revenue from all tech businesses increases by 2%", None, None)
        new_skill_list.append(tech_specialist)
        real_estate_specialist = self.Skill("real estate specialist", "Revenue from all real estate businesses increases by 2%", None, None)
        new_skill_list.append(real_estate_specialist)
        entrepreneur = self.Skill("entrepreneur", "Open new businesses 5% faster.", None, None)
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
    