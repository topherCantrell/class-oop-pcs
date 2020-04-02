
class Point:
    pass

class NaPoint(Point):
    pass

def pointDouble(p):
    b = p.x*2
    p.x = b
    p = Point()
    p.x = 10
    
b = 3
a = Point()
c = 4
a.x = b
a.y = c
b = 8
pointDouble(a)
print(b)
print(a.x)
