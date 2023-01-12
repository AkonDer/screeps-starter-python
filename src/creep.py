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


class Creep:

    spawn = Helper.near_spawn()

    def __init__(self, creep, source):
        self.source = source
        self.creep = creep

    def harvest_energy(self):
        if self.creep.harvest(self.source) == ERR_NOT_IN_RANGE:
            self.creep.moveTo(self.source)
