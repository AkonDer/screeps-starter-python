from defs import *
from helper import Helper
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
        creep = self.creep
        spawn = self.spawn

        # Проверка полный ли крип
        if creep.store[RESOURCE_ENERGY] == creep.store.getCapacity():
            creep.memory.filling = True

        # Если спавн не полный, то восполнить, если полный, то апгейдить
        if spawn.store[RESOURCE_ENERGY] < spawn.store.getCapacity(RESOURCE_ENERGY):
            self.harvest()
        elif spawn.store[RESOURCE_ENERGY] == spawn.store.getCapacity(RESOURCE_ENERGY):
            self.upgrade()

    def upgrade(self):

        if self.creep.memory.filling:
            if self.creep.transfer(self.creep.room.controller, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                self.creep.moveTo(self.creep.room.controller)
            else:
                if self.creep.store[RESOURCE_ENERGY] == 0:
                    self.creep.memory.filling = False
        else:
            self.harvest_energy()

    def harvest(self):

        if self.creep.memory.filling:
            if self.creep.transfer(self.spawn, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
                self.creep.moveTo(self.spawn)
            else:
                if self.spawn.store[RESOURCE_ENERGY] == self.spawn.store.getCapacity(RESOURCE_ENERGY) \
                        or self.creep.store[RESOURCE_ENERGY] == 0:
                    self.creep.memory.filling = False
        else:
            self.harvest_energy()
