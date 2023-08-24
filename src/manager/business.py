from state_manager import StateManager
from allcities import cities 
import numpy as np
from bank import Transaction, Bank

class Business:
    state = StateManager()

    REVENUE_CONSTANT = 1000000000.00
    #location is a City object from the allcities package
    def __init__(self, name, field, location, scale, quality, variability, stability, employees, start_time, upfront_cost, purchase_value):
        self.name = name
        self.field = field
        self.location = location
        self.upfront_cost = upfront_cost
        self.purchase_value = purchase_value

        #typically in range 0 to 1, but maximum is actually unbounded
        #this reflects the size of the business. businesses with higher scales
        #have higher revenues but higher expenses. 
        self.scale = scale

        #typically in the range 0 to 10, but maximum is actually unbounded
        #this reflects how "good" the business is. How well-made are the products,
        #how skilled the employees, etc. In effect, this determines the profit margin.
        #A value of 1 means that the business breaks even on average. Businesses will usually
        #start below 1.
        self.quality = quality 

        #affects how much revenue might deviate from expected. This is a net neutral quality, as the expected revenue
        #is unchanged. Some managers, however, may prefer higher or lower variability (I'd prefer lower).
        #0 means it will be exactly the expected. 1 will operate on a bell curve where one standard deviation is 100% of revenue.
        #i.e. 0.15% of the time it will generate 3 standard deviations more than the revenue, meaning 4 times the revenue in total
        #     0.15% of the time it will generate 3 standard deviations less than the revenue, meaning it will generate -2 times the revenue in total.
        self.variability = variability

        #stability determines how resistant your business is to decay. Without intervention, a business
        #will decay (in quality and scale) by 0.5% on average per month. However, with a stability of 1, the business will not decay at all. 
        self.stability = stability 

        #the number of employees. as of now, just a more user-friendly and fun view of the scale. 
        self.employees = employees

        #how long does it take to start this business. only relevant before it begins running
        #this will default at 60 days. Perks, skills, and scale choice will affect this. 
        self.start_time = start_time

        #is the business running yet?
        self.running = True

        #who owns the business (None, until the user buys it?)
        self.owner = None

        #how much money does the business generate per month on average.
        #A business at a scale of 1 will generate 50,000,000,000 (50 billion) per month.
        #A business at a scale of 0 would generate 0 per month.
        #So, monthly_revenue should be 50000000000.00 * scale
        self.default_revenue_amount = Business.REVENUE_CONSTANT * self.scale * self.quality

        #by default, expenses equal revenut
        self.default_expense_amount = self.default_revenue_amount

    def generate_revenue_for(self, manager):
        #provide revenue to manager's bank account
        #use a bell curve, centered at revenue_amount with an adjustment for quality
        std_dev = self.default_revenue_amount * self.variability
        amount = np.random.normal(self.default_revenue_amount, std_dev, None)
        transaction = Transaction(manager.bank, self, amount, Business.state.get_time())
        return transaction
    
    def incur_expenses(self, manager):
        transaction = Transaction(manager.bank, self, -1 * self.default_expense_amount, Business.state.get_time())
        return transaction


    def monthly_update(self):

        #incur expenses
        self.incur_expenses(self.owner)

        #generate revenue
        self.generate_revenue_for(self.owner)

        #update quality and scale according to stability (bell curve)
        quality_change = np.random.normal(0.005, 0.01, None) * (1 - self.stability)
        scale_change = np.random.normal(0.005, 0.01, None) * (1 - self.stability)
        #keep in mind the change could be negative, in which case this update causes an increase
        self.quality = self.quality * (1 - quality_change)
        self.scale = self.scale * (1 - scale_change)

        #update default_revenue according to scale and quality
        self.default_revenue_amount = Business.REVENUE_CONSTANT * self.scale * self.quality