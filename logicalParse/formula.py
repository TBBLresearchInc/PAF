from logicalParse.coordinates_tab import Coordinates_tab
from logicalParse.fnon import FNon
from logicalParse.fweight import FWeight
from logicalParse.rule import Rule
from logicalParse.text import Text
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Formula(Text):

    def __init__(self, sentence):
        Text.__init__(self, sentence)

    def isFormulaWeight(self):
        return self.sentence[0] == "$"

    def isFormulaNon(self):
        return self.sentence[0:3] == "NON"

    def isFormulaResult(self):
        return self.sentence[0] == "("

    def isFormulaRule(self):
        return self.sentence[0:1] == "R"

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def is_alpha(self,s):
        return not(self.is_number(s))


    def to_logical_rule(self, tab, coordinates):
        R = Rule([], coordinates)
        s = self.sentence[2:(len(self.sentence)-1)]
        while len(s) != 0:
            i = 0
            if s[i]=="-":
                yesno=-1
                s= s[1:]
            else:
                yesno=1
            while self.is_alpha(s[i]):
                i += 1

            l = s[0:i]

            j = i+1
            while j<len(s) and self.is_number(s[j]):
                j += 1
            n = int(s[i: j])

            c = Coordinates_tab(n, l).coordinates_to_int()
            R.add_incompatibility(tab, c, yesno)
            s = s[(j + 1):]
        tab.tab[coordinates]=R
        tab.rule_list.row.append(R)


    def to_fweight_formula(self):
        s = self.sentence[1:(len(self.sentence))]
        i = 0
        if s[i]=="-":
                sign=-1
                s= s[1:]
        else:
                sign=1
        while self.is_number(s[i]):
            i += 1
        l = float(s[0:i])
        j = i
        while self.is_alpha(s[j]):
            j += 1
        m = s[i:j]
        k = j
        while k < len(s) and self.is_number(s[k]):
            k += 1
        n = float(s[j:k])
        weight = Weight(l*sign)
        c = Coordinates_tab(n, m).coordinates_to_int()
        f = FWeight(c, weight)
        return f

    def to_fnon_formula(self):
        s = self.sentence[3:(len(self.sentence))]
        i = 0
        while self.is_alpha(s[i]):
            i += 1
        m = s[0: i]
        j = i
        while j < len(s) and self.is_number(s[j]):
            j += 1
        n = float(s[i:j])
        c = Coordinates_tab(n, m).coordinates_to_int()
        f= FNon(c)
        return f

    def fsolve(self, tab, coordinates):
        if self.isFormulaWeight():
            self.to_fweight_formula().weight_solve(tab, coordinates)
        elif self.isFormulaNon():
                self.to_fnon_formula().non_solve(tab, coordinates)
        elif self.isFormulaRule():
            self.to_logical_rule(tab,coordinates)

