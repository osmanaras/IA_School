# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:55:22 2019

@author: osman
"""
from math import pi



class forme :
    # Constructeur
    def __init__(self,c1=None,c2=None,c3=None,c4=None,ray=None):
        
        # Si c_i, r est defini alors on crée une variable d'instance pour 
        # cette forme 
                
        if c1 != None :  
            self.cote_1 = c1
        if c2 != None :
            self.cote_2 = c2
        if c3 != None :
            self.cote_3 = c3
        if c4 != None :
            self.cote_4 = c4
        if ray != None :
            self.rayon = ray            
      
    def aire(self):
        pass
    
    def canInclude(self,obj):
        canIncludeObj = False
        if isinstance(obj,forme):           # On regarde obj est de classe forme ou l'in de ces subclass
            if self.aire() <= obj.aire():   # Si oui alors on compare les aires  
                canIncludeObj = True
    
        return canIncludeObj

class rectangle(forme):
    
    # la classe Rectangle est une sous classe de forme
    def __init__(self,co1,co2):
        super().__init__(c1 = co1 , c2 = co2)    

    # Retourne le perimetre du rectangle instancié
    def perimetre(self):
        return 2 * self.cote_1 + 2 * self.cote_2
    
    # retourne l'aire du rectangle instancié
    def aire(self):
        return self.cote_1 * self.cote_2
    

    
class carre(forme):
    
    # la classe Carre est une sous classe de forme
    
    def __init__(self,c):
        super().__init__(c1 = c)

 
    #retourne le périmetre du carré instancié
    def perimetre(self):
        return 4 * self.cote_1


    #retourne l'aire du carré instancié
    def aire(self):
        return self.cote_1 * self.cote_1

    
class disque(forme):
    
    # la classe disque est une sous classe de forme
    def __init__(self,r):
        super().__init__(ray=r)    # le rayon du disque

    # retourne le périmetre du circle
    def perimetre(self):
        return 2* pi * self.rayon

    # retourne l'aire du cercle
    def aire(self):
        return pi * self.rayon * self.rayon



class cercle(forme):
    
    # la classe cercle est une sous classe de forme
    def __init__(self,r):
        super().__init__(ray=r)    # le rayon du cercle
        
        
    # retourne le périmetre du circle
    def perimetre(self):
        return 2* pi * self.rayon

    # retourne l'aire du cercle
    def aire(self):
        return pi * self.rayon * self.rayon
