#classe de rectangle.
class Rectangle:
    def __init__(self,longeur=10,largeur=4):
        self.lon=longeur
        self.lar=largeur
        self.nom="rectangle"
    def surface(self): #calculer la surface d'un rectangle
        return(self.lon*self.lar)
    def show(self):#Affichage les caracteristiques d'un rectangle
        return "nom:"+self.nom+ ","+ "longeur:"+str(self.lon)+","+"largeur:"+str(self.lar)+","+ "surface:"+str(self.surface())



# heritage carre ====> Rectangle
class Carre(Rectangle):
    def __init__(self,cote=8):
        super().__init__(longeur=cote,largeur=cote)
        self.nom="Carre"  # surchage d'attribut d'instance

r=Rectangle()
c=Carre()

#l'affichage de rectangle
print("la surface de rectangle est:",r.surface())
print(r.show())
#l'affichage de carre
print("la surface de carre est:",c.surface())
print(c.show())




