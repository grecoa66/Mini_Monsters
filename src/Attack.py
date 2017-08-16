'''
Created on Mar 24, 2016

@author: ag877r
'''


from enum import Enum
import abc
import random


DamageType = Enum('DamageTypes', 'HEALING DAMAGING')
Type = Enum('Types', 'Fire, Water, Electric, Normal')

class Move(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def damage_type(self):
        return NotImplemented
    
    @abc.abstractmethod
    def move_type(self):
        return NotImplemented
    
    @abc.abstractmethod
    def health_change(self):
        return NotImplemented
    
    @abc.abstractmethod
    def to_string(self):
        return NotImplemented
    
######## Electric #########
    
class ThunderStrike(Move):
     
    def damage_type(self):
        return DamageType.DAMAGING
    
    def move_type(self):
        return Type.Electric 
    
    def health_change(self):
        move_min = 6
        move_max = 14
        amount = random.choice(range(move_min, move_max))
        return amount
    
    def to_string(self):
        return "thunderstrike"
    
class Shock(Move):
     
    def damage_type(self):
        return DamageType.DAMAGING
    
    def move_type(self):
        return Type.Electric 
    
    def health_change(self):
        move_min = 8
        move_max = 12
        amount = random.choice(range(move_min, move_max))
        return amount
    
    def to_string(self):
        return "shock"

######## Normal #######

class Punch(Move):
  
    def damage_type(self):
        return DamageType.DAMAGING
    
    def move_type(self):
        return Type.Normal 
    
    def health_change(self):
        move_min = 6
        move_max = 14
        amount = random.choice(range(move_min, move_max))
        return amount

    def to_string(self):
        return "punch"
    
class Kick(Move):
  
    def damage_type(self):
        return DamageType.DAMAGING
    
    def move_type(self):
        return Type.Normal 
    
    def health_change(self):
        move_min = 8
        move_max = 10
        amount = random.choice(range(move_min, move_max))
        return amount
    
    def to_string(self):
        return "kick"
    
####### Fire #######

class Burn(Move):
     
    def damage_type(self):
        return DamageType.DAMAGING
    
    def move_type(self):
        return Type.Fire 
    
    def health_change(self):
        move_min = 9
        move_max = 11
        amount = random.choice(range(move_min, move_max))
        return amount
    
    def to_string(self):
        return "burn"    

####### Healing ########

class Heal(Move):
    
    def damage_type(self):
        return DamageType.HEALING
    
    def move_type(self):
        return Type.Normal 
    
    def health_change(self):
        move_min = 5
        move_max = 10
        amount = random.choice(range(move_min, move_max))
        return amount
    
    def to_string(self):
        return "heal"
