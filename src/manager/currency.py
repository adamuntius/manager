#class for the types of currency (money, xp, etc.?)
class Currency:
    def __init__(self, name):
        self.name = name

class Money(Currency):
    def __init__(self, name, value):
        Currency.__init__(self, name)
        self.value = value
    def set_value(self, value):
        self.value = value
    def get_value(self):
        return self.value
    def get_value_str(self):
        return "$" + str(self.value)

class ManXP(Currency):
    def __init__(self, name, value):
        Currency.__init__(self, name)
        self.value = value
    def set_value(self, value):
        self.value = value
    def get_value(self):
        return self.value
    def get_value_str(self):
        return str(self.value)

class FieldXP(Currency):
    def __init__(self, name, value):
        Currency.__init__(self, name)
        self.value = value
    def set_value(self, value):
        self.value = value
    def get_value(self):
        return self.value
    def get_value_str(self):
        return str(self.value)



