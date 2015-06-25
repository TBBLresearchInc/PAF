from LogicalEngine.PredicateRow import PredicateRow
from logicalParse.predicate import Predicate

__author__ = 'claraberard'


class Rule:

    list = []
    coordinates = (0,0)

    def __init__(self, list, coordinates):
        self.list = list
        self.coordinates = coordinates


    def add_incompatibility(self, tab, coordinates,yesno):
        predicate=Predicate(tab.tab[coordinates].text.sentence,yesno)
        self.list.append(predicate)

    def tostring(self):
        s="regle :("
        for predicate in self.list:
            s+= predicate.tostring()+", "
        return s+")"

    def case_to_predrow(self):
        res=PredicateRow([])
        for case in self.list:
            res.row.append(case.text)
        return res