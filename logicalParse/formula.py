from logicalParse.case import Case

__author__ = 'claraberard'


class Formula(Case):

    def isFormulaWeight(self):
        return self.sentence[0] == '&'

    def solution(self):
        if self.isFormulaWeight():
            begin
            l = FWeight(self.coordinates,self.sentence)




