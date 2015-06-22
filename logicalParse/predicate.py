from logicalParse.text import Text
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Predicate(Text):

    weight = Weight(0)

    def __init__(self):
        self.nature = 1

    def getPredicate(self):
        return self.sentence

    def setPredicate(self, newPredicate):
        self.sentence = newPredicate