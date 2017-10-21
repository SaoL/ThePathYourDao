"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom

from commands.chargen import chargenCmdSet


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """




class start(Room):
    """
    The starting point
    """
    def at_object_creation(self):
        self.cmdset.add(chargenCmdSet, permanent=True)

class dungeon(Room):
    """
    Standard dungeon room
    """
    def at_object_creation(self):
        pass

class town(Room):
    def at_object_creation(self):
        pass

class wild(Room):
    """
    Standard room
    """
