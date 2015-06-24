__author__ = 'claraberard'


class Rule:

    list = []
    coordinates = (0,0)

    def __init__(self, list, coordinates):
        self.list = list
        self.coordinates = coordinates

    def add_incompatibility(self, tab, coordinates):
        print coordinates
        self.list.append(tab.tab[coordinates])

    def tostring(self):
        s="regle :("
        for predicate in self.list:
            s+= predicate.tostring()+", "
        return s+")"