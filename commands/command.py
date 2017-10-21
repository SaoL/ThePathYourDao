"""
Commands

Commands describe the input the player can do to the game.

"""

from evennia import Command as BaseCommand
# from evennia import default_cmds
from evennia import create_object
import random

class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """
# Game commands
class CmdDistSP(Command):
    """
    Distributes skill points

    Usage:
        /distSP
    """
    key = "/distSP"
    aliases = ["/dsp"]
    help_category = "Game"

    def func(self):
        errmsg = "Choose a NUMBER less or equal to your skill points available"
        statPoints = self.caller.db.statPoints

        qPoints = yield("How many points do you want to set?")
        try:
            qPoints = int(qPoints)
        except ValueError:
            self.msg(errmsg)
            return

        if(statPoints == 0) or (qPoints > statPoints):
            self.msg(errmsg)
            return

        stat = yield("To which stat?")
        if stat.lower() not in ("hp","mp","sta","str","vit"):
            self.msg("Use: HP, MP, STA, STR or VIT")
            return

        if stat.lower() == "hp":
            self.caller.db.hp += qPoints * 10
            self.caller.db.statPoints -= qPoints
            getStats(self)
        elif stat.lower() == "mp":
            self.caller.db.mp += qPoints * 5
            self.caller.db.statPoints -= qPoints
            getStats(self)
        elif stat.lower() == "sta":
            self.caller.db.sta += qPoints * 2
            self.caller.db.statPoints -= qPoints
            getStats(self)
        elif stat.lower() == "str":
            self.caller.db.str += qPoints
            self.caller.db.statPoints -= qPoints
            getStats(self)
        elif stat.lower() == "vit":
            self.caller.db.vit += qPoints
            self.caller.db.statPoints -= qPoints
            getStats(self)
        else:
            self.msg("Nothing changed?")

class CmdStats(Command):
    """
    Get stats
    """
    key = "/stat"
    aliases = ["/s"]
    help_category = "Game"

    def func(self):
        getStats(self)

# Methods
def getStats(self):
    caller = self.caller
    msg = ("HP: %i MP: %i STA: %i STR: %i VIT: %i" % (caller.db.hp, caller.db.mp, caller.db.sta, caller.db.str, caller.db.vit))
    caller.msg(prompt=msg)

# Tests
class CmdTest(Command):
    """
    Test command

    Use to test
    """
    key = "test"
    help_category = "Test"

    def func(self):
        answer = yield("apa")
        if answer.lower() in ("apa","shit"):
            self.msg("apeshit")
        else:
            self.caller.msg("din mamma")

class CmdCreateNPC(Command):
    """
    create a new npc

    Usage:
        +createNPC <name>

    Creates a new, named NPC. The NPC will start with a Power of 1.
    """
    key = "+createnpc"
    aliases = ["+createNPC"]
    locks = "call:not perm(nonpcs)"
    help_category = "mush"

    def func(self):
        "creates the object and names it"
        caller = self.caller
        if not self.args:
            caller.msg("Usage: +createNPC <name>")
            return
        if not caller.location:
            # may not create npc when OOC
            caller.msg("You must have a location to create an npc.")
            return
        # make name always start with capital letter
        name = self.args.strip().capitalize()
        # create npc in caller's location
        npc = create_object("characters.Character",
                      key=name,
                      location=caller.location,
                      locks="edit:id(%i) and perm(Builders);call:false()" % caller.id)
        # announce
        message = "%s created the NPC '%s'."
        caller.msg(message % ("You", name))
        caller.location.msg_contents(message % (caller.key, name),
                                                exclude=caller)
