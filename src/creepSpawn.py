from defs import *
from helper import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


class CreepSpawn:

    def __init__(self):
        self.spawn = Helper.near_spawn()
        self.creep_harvester_max = 3

    def run(self):
        if self.creep_count() < self.creep_harvester_max:
            self.spawn.createCreep([WORK, WORK, CARRY, MOVE], None, {"role": "Harvester", "filling": False})

    @staticmethod
    def creep_count():
        num_harvesters = 0
        for name in Object.keys(Game.creeps):
            creep = Game.creeps[name]
            if creep.memory.role == "Harvester":
                num_harvesters += 1
        return num_harvesters
