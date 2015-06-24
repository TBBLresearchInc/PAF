#!/usr/bin/python

from logicalParse.coordinates_tab import Coordinates_tab
from logicalParse.rule import Rule

__author__ = 'claraberard'


class Text:
    nature = 0
    sentence = ""

    def __init__(self, sentence,coordinate):
        self.sentence = sentence
        self.nature = 0
        self.coordinate=coordinate

    def have_weight(self):
        return 0

    @property
    def is_a_predicate(self):
        if self.sentence[0].isalpha():
            self.nature = 1
            return True
        else:
            return False

    @property
    def is_a_attitude(self):
        if self.have_weight()!=0:
            self.nature = 2
            return True
        else:
            return False

    @property
    def is_a_formula(self):
        if self.sentence[0] == "=":
            self.nature = 4
            return True
        else:
            return False
