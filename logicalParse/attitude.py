from logicalParse.coordinates import Coordinates
from logicalParse.predicate import Predicate
from logicalParse.weight import Weight
from logicalParse.text import Text


__author__ = 'claraberard'


class Attitude(Predicate):

    def __init__(self):
        self.nature = 2

    def __init__(self, predicate,coordinates, weight):
        self.predicate=predicate
        self.coodinates=coordinates
        self.weight=weight

