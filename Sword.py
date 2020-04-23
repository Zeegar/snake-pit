# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:14:16 2020

@author: P.Hutchison
"""



class Weapon :
    "Basic physical attacking weapon."
    
    def __init__(self, name,condition,condition_mod,base_damage,element,proficiency_bonus,hit_counter):
        self.name = name
        self.condition = condition
        self.condition_mod = condition_mod
        self.base_damage = base_damage
        self.element = element
        self.proficiency_bonus = proficiency_bonus
        self.hit_counter = hit_counter
        self.damage_out = (base_damage + condition_mod)* proficiency_bonus
 
    
    
    
    
def damage_out(self): 
    return self.damage_out
        
    
wep_1 = ("Sword","dull",0,20,"physical",1,0.0)
  
   

print (wep_1.damage_out())