from logicalParse.coordinates import Coordinates
from logicalParse.text import Text


__author__ = 'claraberard'


class Case():

    coordinates = Coordinates(0,0)
    nature = 0
    text = Text("")
    ref_predicate = coordinates
    ref_non = coordinates

    def __init__(self, row, column, text):
        self.coordinates = Coordinates(row, column)
        self.nature = 0
        self.text = text
        self.ref_predicate = self.coordinates
        self.ref_non = self.coordinates

    def is_predicate(self):
        return self.nature == 1

    def is_attitude(self):
        return self.nature == 2

    def is_rule(self):
        return self.nature == 3

    def is_formula(self):
        return self.nature == 4

    def get_weight(self):
        return self.text.have_weight()

    def is_in_relation(self):
        return (self.ref_predicate != self.coordinates) | (self.ref_non != self.coordinates)


