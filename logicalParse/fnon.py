from logicalParse.attitude import Attitude

__author__ = 'claraberard'

class FNon():
    coordinates = (0, 0)

    def __init__(self, coordinates):
        self.coordinates=coordinates

    def non_solve(self, tab, casedepart):
        """
        :rtype : object
        """
        weight = - tab[self.coordinates].get_weight()
        t = tab[casedepart.coordinates].text
        a = Attitude(t, weight)
        tab[self.coordinates].text = a
        tab[casedepart.coordinates].ref_non = self.coordinates
        tab[self.coordinates].ref_non = casedepart.coordinates
        tab[casedepart].nature = 2