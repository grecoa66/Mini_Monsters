'''
Created on Mar 22, 2016

A trainer will have a name and 3 mini monsters

@author: ag877r
'''

from src import Character

class Trainer(Character.Character):

    def __init__(self, name):
        super().__init__(name)
       
    def desc(self):
        print("Trainer %s is ready for battle!" % self.name)