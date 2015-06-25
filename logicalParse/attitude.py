from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Attitude(Predicate):

    #une attitude est definie comme un predicat ayant un poids

    weight = Weight(0)

    def __init__(self, sentence, weight, coordinates,yesno):
        Predicate.__init__(self, sentence,yesno)
        self.weight = weight

    #pour obtenir le poids de l'attitude

    def get_weight(self):
        return self.weight

    def tostring(self):
        return "attitude:[" + self.sentence + "," +str(self.weight.value) +", " + str(self.yesno) + "]"

    def __name__(self):
        return "attitude"