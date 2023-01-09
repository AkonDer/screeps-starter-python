from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


class CreepSpawn:
    creeps_max = 3
    creep_body = [WORK, CARRY, MOVE, MOVE]

    @classmethod
    def run(cls):
        spawn = Game.spawns.Spawn1
        num_creeps = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName)
        if num_creeps < cls.creeps_max:
            spawn.createCreep(cls.creep_body, None, {"role": "Harvester"})
