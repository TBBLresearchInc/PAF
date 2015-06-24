from logicalParse import Coordinates
from logicalParse.attitude import Attitude
from logicalParse.weight import Weight

__author__ = 'claraberard'


class FWeight():

    weight = Weight(0)
    coordinates = Coordinates(0, 0)

    def __init__(self, coordinates, weight):
        self.coordinates = coordinates
        self.weight = weight

    def weight_solve(self, tab, coordinates):
        t = tab[self.coordinates].text
        yesno = tab[self.coordinates].yesno
        a = Attitude(t, self.weight, yesno)
        tab[coordinates].text = a
        tab[coordinates].ref_predicate = self.coordinates
        tab[self.coordinates].ref_predicate = coordinates