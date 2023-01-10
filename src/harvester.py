from defs import *

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
        if creep.memory.filling is True and creep.store[RESOURCE_ENERGY] < creep.store.getCapacity():
            print(creep.store[RESOURCE_ENERGY])
            if creep.harvest(source) == ERR_NOT_IN_RANGE:
                creep.moveTo(source)
        else:
            creep.memory.filling = True

        if creep.memory.filling:
            pass
        else:
            print(creep.store[RESOURCE_ENERGY])
            if creep.harvest(source) == ERR_NOT_IN_RANGE:
                creep.moveTo(source)
