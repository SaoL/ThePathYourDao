from evennia import Command
from evennia import CmdSet
from evennia import default_cmds


class CmdHatch(Command):
    """
    Start the character creation process

    Usage:
        Hatch
    """
    key = "hatch"
    help_category = "Character creation"

    def func(self):
        pass



class chargenCmdSet(CmdSet):
    """
    Used at starting point
    """
    def at_cmdset_creation(self):
        self.add(CmdHatch())
