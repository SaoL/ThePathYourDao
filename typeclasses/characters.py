"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter

import random

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(player) -  when Player disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Player has disconnected"
                    to the room.
    at_pre_puppet - Just before Player re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "PlayerName has entered the game" to the room.

    """
    def at_object_creation(self):
        self.db.hp = 0
        self.db.mp = 0
        self.db.sta = 0
        self.db.str = 0
        self.db.vit = 0
        self.db.isDead = False
        self.db.statPoints = random.randint(4,6)

    def get_stats(self):
        return self.db.hp, self.db.mp, self.db.sta, self.db.str, self.db.vit
