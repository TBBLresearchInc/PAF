from logicalParse import Coordinates

__author__ = 'claraberard'


class Rule:

    list = []
    coordinates = Coordinates(0,0)

    def __init__(self, list):
        self.list = list

    def add_incompatibility(self, tab, coordinates):
        self.list.append(tab[coordinates])

    def tostring(self):
        s="regle :("
        for predicate in self.list:
            s+= predicate.tostring()+", "
        return s+")"