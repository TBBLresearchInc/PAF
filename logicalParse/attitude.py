from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Attitude():

    weight = Weight(0)

    def __init__(self, weight,predicate):
        self.predicate=predicate
        self.weight = Weight(weight)

    def have_weight(self):
        return self.weight
