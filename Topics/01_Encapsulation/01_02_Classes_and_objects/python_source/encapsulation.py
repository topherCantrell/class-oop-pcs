
class Clock:
    
    def __init__(self,h,m,s):        
        self.hours = h
        self.minutes = m
        self.seconds = s        
         
    # READONLY (no setters)
    
    def get_hours(self):
        return self.hours
            
c = Clock(23,59,59)

h = c.get_hours()

