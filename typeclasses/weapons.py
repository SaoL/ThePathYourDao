from evennia import DefaultObject
from typeclasses.weapon_dict import *


class Weapon(DefaultObject):
   "Weapon"
   def at_object_creation(self):
       "Called whenever a new object is created"

       if self.name in weapon_dict:
           w = weapon_dict[self.name]

       self.ndb.atk = w.atk
       self.ndb.skill = w.skill
