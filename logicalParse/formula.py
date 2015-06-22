from logicalParse.case import Case

__author__ = 'claraberard'


class Formula(Case):

    def isFormulaWeight(self):
        return self.get_inside()[0] == '&'

    def isFormulaNon(self):
        return self.get_inside()[0:2] == "NON"

    def isFormulaResult(self):
        return self.get_inside()[0] == "("



