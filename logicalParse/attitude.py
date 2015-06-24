from logicalParse.predicate import Predicate
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Attitude(Predicate):

    weight = Weight(0)

    def __init__(self, sentence,yesno, weight):
        Predicate.__init__(self, sentence, yesno)
        self.weight = weight


    def have_weight(self):
        return self.weight


    def tostring(self):
        return  "attitude : ("+ self.sentence+", "+ str(self.yesno)+", "+ self.weight.tostring()+")"
