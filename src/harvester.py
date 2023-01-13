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


class Harvester(Creep):

    def __init__(self, creep, source):
        super().__init__(creep, source)

    def run(self):

        self.is_creep_filling()

        # Если спавн не полный, то восполнить, если полный, то апгейдить
        if self.spawn.store.getFreeCapacity(RESOURCE_ENERGY) > 0:
            self.harvest()
        elif self.spawn.store.getFreeCapacity(RESOURCE_ENERGY) == 0:
            self.upgrade()

    def upgrade(self):
        """Апгрейд контроллера"""
        if self.creep.memory.filling:
            if self.creep.transfer(self.creep.room.controller, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                self.creep.moveTo(self.creep.room.controller)
            else:
                if self.creep.store[RESOURCE_ENERGY] == 0:
                    self.creep.memory.filling = False
        else:
            self.harvest_energy()

    def harvest(self):
        """Снабжение спавна энергией"""
        if self.creep.memory.filling:
            if self.spawn.store.getFreeCapacity() != 0 \
                    and self.creep.transfer(self.spawn, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                self.creep.moveTo(self.spawn)
            else:
                if self.spawn.store.getFreeCapacity(RESOURCE_ENERGY) == 0 \
                        or self.creep.store[RESOURCE_ENERGY] == 0:
                    self.creep.memory.filling = False
        else:
            self.harvest_energy()
