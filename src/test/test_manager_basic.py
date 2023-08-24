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
import pytest


def test_attributes():
    man = Manager("adam")
    assert(man.name == "adam")

def test_business_attributes():

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

    #see how the quality has changed
    quality = tb1.quality
    #this should be true like 99.9% of the time
    assert(quality > .70 and quality < .78)

    #see how the scale has changed
    scale = tb1.scale
    #again, should be true like 99.9% of the time
    assert(scale < 0.0000012 and scale > 0.0000005)
    print(scale)
    
    #we've checked that low stability will likely decrease quality and scale, let's set it to 1 now for consistency
    tb1.stability = 1
    sm.update_time()
    new_quality = tb1.quality
    new_scale = tb1.scale
    assert(new_quality == quality)
    assert(new_scale == scale)


    #make sure that variability does its job
    current_average_rev = tb1.default_revenue_amount
    variances = []
    for i in range(0, 10):
        sm.update_time()
        amt = man_1.bank.transactions[-1].amount
        variances.append((amt - current_average_rev) * (amt - current_average_rev)) 
    avg_var = sum(variances) / len(variances)

    tb1.variability = 0.05
    current_average_rev = tb1.default_revenue_amount
    variances = []
    for i in range(0, 10):
        sm.update_time()
        amt = man_1.bank.transactions[-1].amount
        variances.append((amt - current_average_rev) * (amt - current_average_rev)) 
    reduced_avg_var = sum(variances) / len(variances)
    
    assert(reduced_avg_var < avg_var)

    #now let's set variability to 0 for testing and check the effect of quality and scale
    tb1.quality = tb1.quality * 1.50
    sm.update_time()
    new_rev = tb1.default_revenue_amount
    assert new_rev == pytest.approx(current_average_rev * 1.5)
    tb1.scale = tb1.scale * 1.50
    sm.update_time()
    new_rev_2 = tb1.default_revenue_amount
    assert new_rev_2 == pytest.approx(new_rev * 1.50)