'''
Created on Mar 22, 2016

A Mini_Monster will have a name, Health points, 1 or more attacks

@author: ag877r
'''
from src import Character
from src.Attack import DamageType

class Mini_Monster(Character.Character):
    
    alive = True

    def __init__(self, name, health_points, level, move_1, move_2, move_3):
        super().__init__(name)
        self.health_points = health_points
        self.level = level
        self.move_1 = move_1
        self.move_2 = move_2
        self.move_3 = move_3
        self.attacks = {}
        self.attacks.update({str(move_1.to_string(self)): move_1})
        self.attacks.update({str(move_2.to_string(self)): move_2})
        self.attacks.update({str(move_3.to_string(self)): move_3})

    def attack(self, oponent):
        while True:       
            try:
                print("%s's moves are %s, %s, and %s." % (self.name, self.move_1.to_string(self), self.move_2.to_string(self), self.move_3.to_string(self)))
                move_str = str.lower(input("Enter a move! "))
            except NameError:
                print()
                
               
            if move_str in self.attacks:
                move = self.attacks[move_str]
                break
            else:
                print("That move does not exist! Try again.")
        if move.damage_type(self) is DamageType.HEALING:
            damage = self.calc_damage(move)
            self.health_points += damage
            print("%s has healed %i damage. Current health points: %i" % (self.name, damage, self.health_points))
        else:
            damage = self.calc_damage(move)
            oponent.health_points -= damage
            print("%s has taken %i damage. Current health points: %i" % (oponent.name, damage, oponent.health_points))
            
            
    def calc_damage(self, move):
        damage = int(move.health_change(self) * (self.level * .2))
        return damage
        
    def isDead(self):
        dead = False
        if self.health_points <= 0:
            dead = True
        else:
            dead = False
        return dead
    