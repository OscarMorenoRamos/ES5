# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:38:28 2020

@author: loren,Oscar
"""

class Player:
    
    def __init__(self,nom:str):
        self.nom = nom
        self.npunts = 0
        
    def get_nom(self)->str:
        return self.nom
    
    def get_points(self)->int:
        return self.npunts
    
    def is_equal(self,player)->bool:
        return self.nom == player.nom
    
    def add_point(self)->None:
        self.npunts = self.npunts+1
        
    