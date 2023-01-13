from defs import *
from harvester import Harvester
from builder import Builder
from creepSpawn import CreepSpawn

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def main():
    """ Main game logic loop. """

    CreepSpawn().run()

    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        sources = creep.pos.findClosestByRange(FIND_SOURCES)
        if creep.memory.role == "Harvester":
            Harvester(creep, sources).run()
        elif creep.memory.role == "Builder":
            Builder(creep, sources).run()


module.exports.loop = main
