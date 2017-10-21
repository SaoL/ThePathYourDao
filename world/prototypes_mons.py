"""
Possible keywords are:
    prototype - string pointing to parent prototype of this structure.
    key - string, the main object identifier.
    typeclass - string, if not set, will use `settings.BASE_OBJECT_TYPECLASS`.
    location - this should be a valid object or #dbref.
    home - valid object or #dbref.
    destination - only valid for exits (object or dbref).

    permissions - string or list of permission strings.
    locks - a lock-string.
    aliases - string or list of strings.

    ndb_<name> - value of a nattribute (the "ndb_" part is ignored).
    any other keywords are interpreted as Attributes and their values.

See the `@spawn` command and `evennia.utils.spawner` for more info.

"""
from random import randint

GOBLIN = {
"key": "Goblin"
"typeclass": "typeclasses.monsters.goblin"
"level": randint(4,6)
"hp": randint(6,10)
"sta": 20


}
