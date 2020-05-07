# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:33:26 2020

@author: loren,Oscar
"""
import Player

class Game:
    
    def __init__ (self,player1:Player,player2:Player):
        self.player1 = player1
        self.player2 = player2
        
    def get_score(self)->str:
        punts_player1 = self.player1.get_points()
        punts_player2 = self.player2.get_points()
        
        if punts_player1>punts_player2:
            if punts_player1 == 1:
                return "Fifteen-Love"
            if punts_player1 == 2:
                if punts_player2 == 0:
                    return "Thirty-Love"
                else:
                    return "Thirty-Fifteen"
            if punts_player1 == 3:
                if punts_player2 == 0:
                    return "Forty-Love"
                if punts_player2 == 1:
                    return "Forty-Fifteen"
                else:
                    return "Forty-Thirty"
            if punts_player1 > 3 and punts_player2 == (punts_player1-1):
                return "Advantage player1"
            else:
                return "Win for player1"
            
        if punts_player2>punts_player1:
            if punts_player2 == 1:
                return "Love-Fifteen"
            if punts_player2 == 2:
                if punts_player1 == 0:
                    return "Love-Thirty"
                else:
                    return "Fifteen-Thirty"
            if punts_player2 == 3:
                if punts_player1 == 0:
                    return "Love-Forty"
                if punts_player1 == 1:
                    return "Fifteen-Forty"
                else:
                    return "Thirty-Forty"
            if punts_player2 > 3 and punts_player1 == (punts_player2-1):
                return "Advantage player2"
            else:
                return "Win for player2"
        else:
          if punts_player1 == 0:
              return "Love-All"
          if punts_player1 == 1:
              return "Fifteen-All"
          if punts_player1 == 2:
              return "Thirty-All"
          else:
              return "Deuce"
              
          
            
    def won_point(self,player:Player)->None:
        
        if self.player1.is_equal(player):
            self.player1.add_point()
        else:
            self.player2.add_point()
        
            
    
            