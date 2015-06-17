from logicalParse.predicate import Predicate

__author__ = 'claraberard'


class Attitude(Predicate):

    def setWeight(self,newweight):
        self.weight=newweight

    def getWeight(self):
        return self.weight

