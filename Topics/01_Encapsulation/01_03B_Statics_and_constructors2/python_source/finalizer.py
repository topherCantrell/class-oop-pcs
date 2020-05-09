
class Point:
    
    def __init__(self,x,y):
        self._x = x
        self._y = y
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
                
    def add_to_x_y(self,value):
        ret = Point(self._x+value,self._y+value)
        return ret
    
    def __add__(self,value):
        ret = Point(self._x+value,self._y+value)
        return ret        
    
    def __eq__(self,other):
        if other._x == self._x and other._y == self._y:
            return True
        return False
    
    def __setitem__(self,ind,value):
        self._x = ind
        self._y = value
        
a = Point(1,2)

b = a.add_to_x_y(5)
c = a+5

print(b.get_x())
print(c.get_x())

print(b == c)

a[24] = 30

print(a.get_x(),a.get_y())
