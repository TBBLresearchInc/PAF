from logicalParse.coordinates import Coordinates
from logicalParse.formula import Formula
from logicalParse.text import Text

__author__ = 'claraberard'

class Case():

    coordinates = Coordinates(0,0)
    text = Text("")
    ref_predicate = coordinates
    ref_non = coordinates

    def __init__(self, coordinates, text):
        self.coordinates = coordinates
        self.text = text
        self.ref_predicate = self.coordinates
        self.ref_non = self.coordinates

    def get_weight(self):
        return self.text.have_weight()

    def is_in_relation(self):
        return (self.ref_predicate != self.coordinates) | (self.ref_non != self.coordinates)

    def to_logical_rule(self):
        return Formula(self.text).to_logical_rule()


