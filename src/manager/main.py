from manager import Manager
import time
from state_manager import StateManager 
from datetime import datetime, timedelta
from game_time import GameTime
import threading

new_man = Manager("adam")
state = StateManager()
state.set_time(GameTime(None, None, None, datetime.now()))
print(state.get_time())

#update time with a thread
def update_time(state):
    for i in range(3):
        time.sleep(5)
        new_time = state.get_time() + timedelta(days=1)
        state.set_time(GameTime(None, None, None, new_time))
        print(state.get_time())
time_thread =  threading.Thread(target=update_time, args=(state,))
time_thread.start()
time_thread.join()