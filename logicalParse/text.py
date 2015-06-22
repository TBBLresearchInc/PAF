from logicalParse.coordinates import Coordinates
from logicalParse.case import Case

__author__ = 'claraberard'

class Text:

    nature = 0
    sentence = ""

    def __init__(self, sentence):
        self.sentence = sentence
        self.nature = 0

    def is_predicate(self):
        return self.nature == 1

    def is_attitude(self):
        return self.nature == 2

    def is_rule(self):
        return self.nature == 3

    def is_formula(self):
        return self.nature == 4








