from logicalParse.attitude import Attitude
from logicalParse.formula import Formula

__author__ = 'claraberard'


class FWeight(Formula):

    def solveFormula(self):
        return Attitude(self.coordinates, self.sentence[1:])
