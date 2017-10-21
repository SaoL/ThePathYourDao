
from typeclasses.objects import Object

class goblin(Object):
    """
    This creates a simple goblin
    """
    def at_object_creation(self):
        "this is called only once, when object is first created"
        self.db.desc = "This is a pretty rose with thorns."
