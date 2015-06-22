from logicalParse import Coordinates
from logicalParse.attitude import Attitude
from logicalParse.formula import Formula
from logicalParse.weight import Weight

__author__ = 'claraberard'


class FWeight(Formula):
    weight = Weight(0)
    coordinates = Coordinates(0, 0)

    def __init__(self, coordinates, weight):
        self.coordinates = coordinates
        self.weight = weight

    def weight_solve(self, tab, casedepart):
        t = tab[casedepart.coordinates].text
        a = Attitude(t, self.weight)
        tab[self.coordinates].text = a
        tab[casedepart.coordinates].ref_predicate = self.coordinates
        tab[self.coordinates].ref_predicate = casedepart.coordinates
        tab[casedepart].nature = 2
