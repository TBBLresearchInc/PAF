from logicalParse.attitude import Attitude
from logicalParse.formula import Formula
from logicalParse.predicate import Predicate

__author__ = 'claraberard'


class FWeight(Formula):

    def solveFormula(self):
        p = Predicate( self.sentence[1:])
        return Attitude(self.coordinates, )
