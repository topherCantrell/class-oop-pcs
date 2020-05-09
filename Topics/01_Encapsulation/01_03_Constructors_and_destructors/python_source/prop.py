  
class Point:
            
    def __init__(self):
        self.x = 0 # Calls setter
            
    @property
    def x(self):
        print('In getter')
        return self._x
    
    @x.setter
    def x(self,x):
        print('In setter')
        self._x = x
    
p = Point()
        
p.x = 25
    
print(p.x)
    
