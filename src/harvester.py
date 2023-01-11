from defs import *
from helper import Helper

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


class Harvester:

    @staticmethod
    def run(creep, source):

        spawn = Helper.near_spawn()

        # Проверка полный ли крип
        if creep.store[RESOURCE_ENERGY] == creep.store.getCapacity():
            creep.memory.filling = True

        if spawn.store[RESOURCE_ENERGY] < spawn.store.getCapacity(RESOURCE_ENERGY):
            creep.memory.role = "Harvester"
        elif spawn.store[RESOURCE_ENERGY] == spawn.store.getCapacity(RESOURCE_ENERGY):
            creep.memory.role = "Upgrade"

        if creep.memory.role == "Upgrade":
            if creep.memory.filling:
                if creep.transfer(creep.room.controller, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                    creep.moveTo(creep.room.controller)
                else:
                    if creep.store[RESOURCE_ENERGY] == 0:
                        creep.memory.filling = False
            else:
                if creep.harvest(source) == ERR_NOT_IN_RANGE:
                    creep.moveTo(source)

        if creep.memory.role == "Harvester":
            if creep.memory.filling:
                if creep.transfer(spawn, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                    creep.moveTo(spawn)
                else:
                    if spawn.store[RESOURCE_ENERGY] == spawn.store.getCapacity(RESOURCE_ENERGY) \
                            or creep.store[RESOURCE_ENERGY] == 0:
                        creep.memory.filling = False
            else:
                if creep.harvest(source) == ERR_NOT_IN_RANGE:
                    creep.moveTo(source)

