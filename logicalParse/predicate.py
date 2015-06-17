from logicalParse.text import Text
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Predicate(Text):

    weight = Weight(1)


    def getPredicat(self):
        return self.sentence

    def setPredicat(self, newPredicat):
        self.sentence = newPredicat