from manager import Manager
import time
from state_manager import StateManager 
from datetime import datetime, timedelta
from game_time import GameTime
import threading
from field import FieldSetup
from business import Business
from allcities import cities

new_man = Manager("adam")
state = StateManager()
state.set_time(GameTime(None, None, None, datetime.now()))
state.bus_fields = FieldSetup.init_bus_fields()
greensboro = cities.filter(name="greensboro", admin1_code="NC")
tech_business = Business("adam_tech", state.bus_fields[0], greensboro, 0.001, 1.05, 0.1, .50, 100, 50)
print(state.get_time())

#update time with a thread
def update_time(state):
    for i in range(3):
        time.sleep(5)
        new_time = state.get_time() + timedelta(days=1)
        state.set_time(GameTime(None, None, None, new_time))
        t = tech_business.generate_revenue_for(new_man)
        tr = tech_business.incur_expenses(new_man)
        print(t.amount, t.datetime)
        print(tr.amount, tr.datetime)
        print(state.get_time())
time_thread =  threading.Thread(target=update_time, args=(state,))
time_thread.start()
time_thread.join()