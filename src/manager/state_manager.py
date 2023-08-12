import threading

class StateManager:
    #enforce Singleton state pattern
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(StateManager, cls).__new__(cls)
            
            #set up game state
            cls.instance.manager = None
            cls.instance.date = None

            #the date/time may be accessed asynchronously, so it needs a lock
            cls.instance.date_lock = threading.Lock()
        return cls.instance
    
    def get_time(self):
        with self.date_lock:
            return self.date.date_time
        
    def set_time(self, game_time):
        with self.date_lock:
            self.date = game_time

        
    
    