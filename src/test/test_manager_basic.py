import sys
import os
sys.path.append(os.path.relpath("../manager"))

from manager import Manager
from business import Business
from field import FieldSetup
from allcities import cities
from collections.abc import Set
from state_manager import StateManager 
from game_time import GameTime
from datetime import datetime, timedelta

def test_attributes():
    man = Manager("adam")
    assert(man.name == "adam")

def test_tech_business_test():

    #set up state
    sm = StateManager()
    sm.set_time(GameTime(None, None, None, datetime.now()))
    sm.bus_fields = FieldSetup.init_bus_fields()

    #set up a tech business
    tech_field = sm.bus_fields[0]
    la_city = cities.filter(name="Los Angeles", admin1_code="CA")
    tb1 = Business(name="Hydrocode", field=tech_field, location=la_city, scale=0.000001, quality=0.75, variability=0.10, stability=0.0, employees=0.05 * 2000, start_time=60, upfront_cost=0, purchase_value=None)
    #set up a manager 
    man_1 = Manager("adam")
    sm.manager = man_1

    #buy a tech business with that manager
    man_1.start_business(tb1, sm.get_time())

    #do a few updates, make sure things are in good range
    for i in range(0, 5):
        sm.update_time()
    
    #1 transaction for starting the business, 5 for revenues, 5 for expenses
    assert(len(man_1.bank.transactions) == 11)

    #make sure the amounts are reasonable
    #TODO:  



