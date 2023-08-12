from datetime import datetime, date, time
class GameTime:

    #initialize with a month, day, and year, or with a datetime.datetime object
    def __init__(self, month, day, year, date_time):
        #if datetime is defined, none of the others should be. If any of the first are defined, datetime should not be.
        if date_time != None and (month != None or day != None or year != None):
            raise Exception("Provide M,D,Y or a datetime object")
        if date_time == None and None in [month, day, year]:
            raise Exception("Provide M,D,Y or a datetime object")
        if date_time == None:
            self.month = month
            self.day = day
            self.year = year
            #we will always zero out the "time" component
            self.date_time = datetime(year, month, day)
        else:
            self.month = date_time.month
            self.day = date_time.day
            self.year = date_time.year
            self.date_time = datetime(self.year, self.month, self.day)

    

