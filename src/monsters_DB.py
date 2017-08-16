'''
Created on Apr 5, 2016

@author: ag877r
'''
import sqlite3
from src.Mini_Monster import Mini_Monster
from src.Attack import *



conn = sqlite3.connect('test.db')

attacks = {"kick":Kick,
           "punch":Punch,
           "shock":Shock,
           "thunderstrike":ThunderStrike,
           "burn":Burn,
           "heal":Heal}

# conn.execute("INSERT INTO MONSTERS (NAME, HEALTH_POINTS, LEVEL, MOVE_1, MOVE_2, MOVE_3) \
#              VALUES('FireBoy3', 25, 3, 'shock', 'kick', 'burn')")
#  
# conn.execute("INSERT INTO MONSTERS (NAME, HEALTH_POINTS, LEVEL, MOVE_1, MOVE_2, MOVE_3) \
#              VALUES('ThunderKid3', 25, 3, 'thunderstrike', 'punch', 'heal')")
#  
# conn.commit()
  



def get_monsters_from_DB():
    
    conn = sqlite3.connect('test.db')
    monsters ={}
    
    cursor = conn.execute("SELECT * from Monsters")
    for row in cursor:
        move_1 = attacks[row[3]]
        move_2 = attacks[row[4]]
        move_3 = attacks[row[5]]
        new_monster = Mini_Monster(row[0], row[1], row[2], move_1, move_2, move_3)
        monsters.update({row[0]: new_monster})
         
    conn.close()
    return monsters

# def put_monster_in_DB(monster):
#     conn = sqlite3.connect('test.db')
#      
#     if isinstance(monster, Mini_Monster) and (monster != None):
#         monster_string =" '%s', %i, $i, '%s', '%s', '$s'" % (monster.name, monster.health_points, monster.level, monster.move_1, monster.move_2, monster.move_3)
#         conn.execute("INSERT INTO MONSTERS (NAME, HEALTH_POINTS, LEVEL, MOVE_1, MOVE_2, MOVE_3) VALUES(%s)" % (monster_string))
           
#get_monsters_from_DB()
monster_123 = Mini_Monster("Kimberly", 23, 4, Kick, Punch, Burn)
#put_monster_in_DB(monster_123)



