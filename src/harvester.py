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


    def __init__(self, creep, source):
        self.creep = creep
        self.source = source

    def creep_harvest_run(cls):
        # if self.creep.store(RESOURCE_ENERGY) < self.creep.store.getCapacity():
        print(cls.creep.store(RESOURCE_ENERGY))
        # if self.creep.harvest(self.source) == ERR_NOT_IN_RANGE:
        #     self.creep.moveTo(self.source)
