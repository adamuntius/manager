from skill_tree import Perk

#class for fields a business could be
class Field:
    def __init__(self, name, description, perks):
        self.name = name
        self.description = description
        self.perks = perks

class FieldSetup:
    def init_bus_fields():
        fields = []
        tech_perks = []
        easy_entry = Perk("easy entry", "businesses cost 25% less to start.", None, None)
        quick_start = Perk("quick start", "businesses begin operating 50% sooner.", None, None)
        high_variability = Perk("high variability", "revenue variability is increased by 50%", None, None)
        low_stability = Perk("low stability", "stability is reduced by 25%", None, None)
        tech_perks.append(easy_entry)
        tech_perks.append(quick_start)
        tech_perks.append(high_variability)
        tech_perks.append(low_stability)
        fields.append(Field("tech", "", tech_perks))
        return fields
    
