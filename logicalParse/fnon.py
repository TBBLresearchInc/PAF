from logicalParse.attitude import Attitude
from logicalParse.predicate import Predicate

__author__ = 'claraberard'

class FNon():
    coordinates = (0, 0)

    def __init__(self, coordinates):
        self.coordinates=coordinates

    def non_solve(self, tab, coordinates):
        """
        :rtype : object
        """
        t = tab.tab[coordinates].text.sentence
        tab.tab[coordinates].text = Predicate(t, 1)
        a = Predicate(t, -1)
        tab.tab[self.coordinates].text = a
        tab.tab[coordinates].ref_non = self.coordinates
        tab.tab[self.coordinates].ref_non = coordinates