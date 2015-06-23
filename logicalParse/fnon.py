from logicalParse import Coordinates
from logicalParse.attitude import Attitude
from logicalParse.formula import Formula

__author__ = 'claraberard'

class FNon(Formula):
    coordinates = Coordinates(0, 0)

    def __init__(self, coordinates, sentence):
        Formula.__init__(self, sentence)
        self.coordinates = coordinates
        
    

    def non_solve(self, tab, casedepart):
        """

        :rtype : object
        """
        weight = - tab[self.coordinates].get_weight()
        t = tab[casedepart.coordinates].text
        a = Attitude(t, self.weight)
        tab[self.coordinates].text = a
        tab[casedepart.coordinates].ref_non = self.coordinates
        tab[self.coordinates].ref_non = casedepart.coordinates
        tab[casedepart].nature = 2