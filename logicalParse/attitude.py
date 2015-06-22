from logicalParse.coordinates import Coordinates
from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Attitude:

    def __init__(self, predicate,coordinates, weight):
        self.predicate=predicate
        self.coodinates=coordinates
        self.weight=weight

