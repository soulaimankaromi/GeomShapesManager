class Rectangle:
    _count = 0 
    def __init__(self, longueur = 0, largeur = 0):
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle._count += 1

    def Getlongueur(self) :
        return self.__longueur
    
    def setlongueur(self, longueur) :
        self.__longueur = longueur 

    def Getlargeur(self) :
        return self.__largeur
    
    def setlargeur(self, largeur) :
        self.__largeur = largeur 

    def Getcount(self) :
        return Rectangle._count
    
    def Equals(self, R1) :
        if self.__largeur == R1.__largeur and self.__longueur == R1.__longueur :
            return True
        else : 
            return False
        
    def Perimetre(self):
        P = (self.__largeur + self.__longueur) * 2 
        return P 
    
    def Surface(self) :
        return self.__largeur * self.__longueur
    
    def ToString (self) :
        return "Largeur :" + str(self.Getlargeur()) + ";  longueur :" + str(self.Getlongueur()) +"; NbrRectangle :"+ str(self.Getcount()) +"."
    
class Parallelepipede (Rectangle) :
    _count1 = 0
    def __init__(self, longueur = 0, largeur = 0, hauter = 0 ):
        super().__init__(longueur, largeur)
        self.__hauter = hauter
        Parallelepipede._count1 += 1

    def Gethauter(self) :
        return self.__hauter
    
    def sethauter(self, hauter) :
        self.__hauter = hauter

    def Getcount1(self) :
        return Parallelepipede._count1

    def Equals(self, P) :
        if self.__largeur == P.__largeur and self.__longueur == P.__longueur and self.__hauter == P.__hauter :
            return True
        else : 
            return False
        
    def Surface(self):
        return super().Surface() * self.__hauter
    
    def ToString (self) :
        return "Largeur :" + str(self.Getlargeur()) + ";  longueur :" + str(self.Getlongueur())+ "; Hauter :"+ str(self.Getcount1()) +"; NbrRectangle :"+ str(self.Getcount()) +"."
    
    def Volume (self) :
        return ( self.Getlargeur() * self.Getlongueur() * self.__hauter)