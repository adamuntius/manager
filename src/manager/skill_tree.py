class Skill:
    def __init__(self, name, description, activation_function, deactivation_function):
        self.name = name
        self.description = description
        self.active = False
        self.activation_function = activation_function
        self.deactivation_function = deactivation_function
    def activate():
        activation_function()
    def deactivate():
        deactivation_function()

class SkillNode:
    def __init__(self, skill, parents, children, purchase_function):
        self.skill = skill
        self.parents = parents
        self.children = children 
        self.cost_conditions = purchase_function

    def add_child(child_node):
        self.children.append(child_node)

    def add_parent(parent_node):
        self.parents.append(parent_node)

#A Perk is like a skill
class Perk(Skill):
    def __init__(self, name, description, activation_function, deactivation_function):
        Skill.__init__(self, name, description, activation_function, deactivation_function)
    pass

class SkillTree:

    def initialize_skill_map(self):
        new_skill_map = {}
        generalist = Skill("generalist", "Revenue from all businesses increases by 1%.", None, None)
        new_skill_map["generalist"] = generalist
        tech_specialist = Skill("tech specialist", "Revenue from all tech businesses increases by 2%", None, None)
        new_skill_map["tech_specialist"] = tech_specialist
        real_estate_specialist = Skill("real estate specialist", "Revenue from all real estate businesses increases by 2%", None, None) 
        new_skill_map["real_estate_specialist"] = real_estate_specialist
        entrepreneur = Skill("entrepreneur", "Open new businesses 5% faster.", None, None)
        new_skill_map["entrepreneur"] = entrepreneur
        return new_skill_map

    def initialize_skill_tree(self):
        skill_map = self.initialize_skill_map()
        root_node = SkillNode(None, None, [], None)
        generalist_node = SkillNode(skill_map["generalist"], root_node, None, None)
        tech_specialist_node = SkillNode(skill_map["tech_specialist"], root_node, None, None)
        real_estate_specialist_node = SkillNode(skill_map["real_estate_specialist"], root_node, None, None)
        entrepreneur_node = SkillNode(skill_map["entrepreneur"], root_node, None, None)
        root_node.add_child(generalist_node)
        root_node.add_child(tech_specialist_node)
        root_node.add_child(real_estate_specialist_node)
        root_node.add_child(entrepreneur_node)
        return root_node

    def print_skill_list(self):
        for skill in self.skill_list:
            print(skill.description)

    def __init__(self, owner_type):
        if owner_type != "business" and owner_type != "owner":
            raise Exception("Invalid owner type for skill tree")
        self.owner_type = owner_type
        self.skill_list = self.initialize_skill_map()