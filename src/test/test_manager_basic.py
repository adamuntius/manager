import sys
import os
sys.path.append(os.path.relpath("../manager"))

from manager import Manager
from business import Business
from field import FieldSetup
from allcities import cities
from collections.abc import Set

def test_attributes():
    man = Manager("adam")
    assert(man.name == "adam")

def test_tech_business_test():
    #set up a tech business
    fields = FieldSetup.init_bus_fields()
    tech_field = fields[0]
    location = cities.filter(name="Los Angeles")
    breakpoint()
    tb1 = Business("Hydrocode", tech_field, )
    #set up a manager 

    #buy a tech business with that manager

