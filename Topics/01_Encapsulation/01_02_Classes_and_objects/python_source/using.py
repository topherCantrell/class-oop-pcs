

class Robot:
    
    def goTo(self,location):
        self.location = location
        battery = battery - 0.10;
        
    def get_location(self):
        return self._location
    
    def _move_left_leg(self):
        pass
    
    def _move_right_leg(self):
        pass
    
    def say_hi(self):
        print('Beep Beep')
        
    def get_battery_level(self):
        return 0.0
    
    def go_to(self,lat: float,lng: float=0) -> None:
        self._move_left_leg()
        self._move_right_leg()
        
class Point:
    
    def addX(self,a):
        return self.x + a
    
p = Point()
a = p.add(5)
        
bob = Robot()
bob.go_to(20)
x = bob.get_location()

jan = Robot()
jan._go_to(50)
y = jan.get_location()

bob._location = 100
        
rob = Robot()

rob.say_hi()

lev = rob.get_battery_level()

rob.go_to(34.738, -86.60)

rob._move_left_leg()


import logging

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.warning('Bad things!')
logger.debug('Starting up')

b = logger.isEnabledFor(logging.WARN)
print(b)