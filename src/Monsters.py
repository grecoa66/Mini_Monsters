'''
Created on Mar 24, 2016

@author: ag877r
'''
from src.Mini_Monster import Mini_Monster
from src.Attack import *


monsters = {}



Jim_Bob = Mini_Monster("Jim Bob", 25, 3, ThunderStrike, Punch, Heal)

Kenny = Mini_Monster("Kenny", 25, 3, Shock, Kick, Burn)

def make_monster():
    monsters.update({"Jim Bob":Jim_Bob})
    monsters.update({"Kenny":Kenny})
    return monsters

