from logicalParse.coordinates import Coordinates
from logicalParse.text import Text

__author__ = 'claraberard'


class Rule(Text):

    def getRule(self):
        return self.sentence

    def setRule(self, newrule):
        self.sentence = newrule










