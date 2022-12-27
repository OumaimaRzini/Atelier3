#classe de vecteur 2D
class Vecteur2D:
    # constructeur
    def __init__(self,x=0,y=0):
     self.x=x
     self.y=y 

    def __str__(self):
        return "x=%d,y=%d" %(self.x,self.y)
        
    def show(self):
        return (self.x , self.y)

# surcharger l'operatuer +
    def __add__(self,other):
        return Vecteur2D(self.x+other.x ,self.y+other.y)


     
print("une instance par defaut:",Vecteur2D())
print("une instance initialisee",Vecteur2D(10,8))

v1=Vecteur2D(1,2)
print("v1",v1.show())
v2=Vecteur2D(1,1)
print("v2",v2.show())

# surcharge d'operateur +
v3=v1+v2
print("v3", v3.show())
