#classe point
class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def show(self):
        return "x="+str(self.x)+ ","+ "y="+ str(self.y)
#classe composite utilisant la classe Point
class Segment:
    def __init__(self,x0,y0,x1,y1):
        self.orig=Point(x0,y0)
        self.extrem=Point(x1,y1)
    def show(self):
        return(self.orig.x,self.orig.y,self.extrem.x,self.extrem.y)

p1=Point(1,2)
print(p1.show())

s= Segment(1,2,3,4)
print(s.show())
