from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Attitude(Predicate):

    weight = Weight(0)

    def __init__(self, sentence, weight):
        self.sentence = sentence
        self.weight = Weight(weight)

    def have_weight(self):
        return self.weight

