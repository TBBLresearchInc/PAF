from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Attitude(Predicate):

    #une attitude est definie comme un predicat ayant un poids

    weight = Weight(0)

    def __init__(self, sentence, weight, yesno):
        Predicate.__init__(self, sentence, yesno)
        self.weight = weight

    #pour obtenir le poids de l'attitude

    def have_weight(self):
        return self.weight

