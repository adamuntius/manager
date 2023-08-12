from state_manager import StateManager

class Business:
    state = StateManager()
    bus_fields = state.get_bus_fields()
    def __init__(name, field):
        self.field = field