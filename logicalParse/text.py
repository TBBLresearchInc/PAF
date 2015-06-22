from logicalParse.coordinates import Coordinates
from logicalParse.case import Case

__author__ = 'claraberard'

class Text:

    nature = 0
    sentence = ""

    def __init__(self, sentence):
        self.sentence = sentence

    def is_predicate(self):
        return self.nature == 1

    def is_Attitude(self):
        return  self.nature == 2

    def is_Rule(self):
        return self.nature == 3

    def is_Formula(self):
        return self.nature == 4



