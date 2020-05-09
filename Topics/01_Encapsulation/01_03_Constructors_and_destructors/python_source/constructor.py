
class Point:
        
    def __init__(self,color,x=0,y=0):
        self._color = color
        self._x = x
        self._y = y
        
    def __repr__(self):
        return f'{self._color} {self._x} {self._y}'
        
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

def addAll(*args,**kwargs):
    print(type(args),args)    
    print(type(kwargs),kwargs)
    
def main():
    
    a = Point('Red')
    print(a)
    b = Point('Blue',5)
    print(b)
    c = Point('Green',y=2)
    print(c)
    d = Point('Pink',3,4)
    print(d)
    
    addAll(1,2,3,name='chris',cool='yes')
    
    #p = Point(7,9)
    
    #print(p.get_x())
    
if __name__ == '__main__':   
    
    main()
    
    