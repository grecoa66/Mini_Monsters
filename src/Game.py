'''
Created on Mar 22, 2016

@author: ag877r
'''

from src.Mini_Monster import Mini_Monster
from src.Trainer import Trainer
from src import Monsters
from src import monsters_DB
         
class Game():
    
    print("Welcome to Mini-Monsters!")
    #get the first players name and instantiate obj
    player_1_name= str(input("Player 1 please enter your name."))
    player_1 = Trainer(player_1_name)
    #get the second players name and instantiate obj
    player_2_name= str(input("Player 2 please enter your name."))
    player_2 = Trainer(player_2_name)
    
    print("Player 1: %s VS. Player 2: %s" % (player_1.name, player_2.name))
    
    #monsters = Monsters.make_monster()
    monsters = monsters_DB.get_monsters_from_DB()
    monster_1 = monsters["Kenny"]
    monster_2 = monsters["Timmy"]
    
    print("%s's monster is name %s."% (player_1.name, monster_1.name))
    print("%s's monster is name %s."% (player_2.name, monster_2.name))
    
    print("The match will now begin! %s, your monster %s will attack first" % (player_1.name, monster_1.name))
    
    while True:
        
        print("%s turn to attack!" % monster_1.name)
        
        monster_1.attack(monster_2)
        if(monster_2.isDead()):
            break;
        
        print("%s's turn to attack!" % monster_2.name)
        monster_2.attack(monster_1)
        if(monster_1.isDead()):
            break;
    
    if monster_1.alive:
        print("%s died" % monster_2.name)
        print("%s has won the match!" % player_1.name)
    else:
        print("%s died" % monster_1.name)
        print("%s has won the match!" % player_2.name)
        
Game()
    