from defs import *
from creep import Creep

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


class Builder(Creep):
    def __init__(self, creep, source):
        super().__init__(creep, source)

    def run(self):

        self.is_creep_filling()

        target = self.creep.room.find(FIND_MY_CONSTRUCTION_SITES)

        if self.creep.memory.filling:
            if self.creep.build(target[0]) == ERR_NOT_IN_RANGE:
                self.creep.moveTo(target[0])
            else:
                if self.creep.store[RESOURCE_ENERGY] == 0:
                    self.creep.memory.filling = False
        else:
            self.harvest_energy()
