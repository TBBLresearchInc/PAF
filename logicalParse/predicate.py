from logicalParse.text import Text
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Predicate(Text):

    weight = Weight(0)

    def __init__(self,sentence,weight):
        self.weight=weight
        self.sentence=sentence

    def getPredicate(self):
        return self.sentence

    def setPredicate(self, newPredicate):
        self.sentence = newPredicate