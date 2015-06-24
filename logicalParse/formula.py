from logicalParse import Coordinates
from logicalParse.coordinates_tab import Coordinates_tab
from logicalParse.fnon import FNon
from logicalParse.fweight import FWeight
from logicalParse.rule import Rule
from logicalParse.weight import Weight

__author__ = 'claraberard'


class Formula():

    def __init__(self, sentence):
        self.sentence = sentence


    def isFormulaWeight(self):
        return self.sentence[0] == '&'

    def isFormulaNon(self):
        return self.sentence[0:2] == "NON"

    def isFormulaResult(self):
        return self.sentence[0] == "("

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def to_logical_rule(self, tab, coordinates):
        """
        :type tab: Tab
        """
        R = Rule([], coordinates)
        s = self.sentence[2:(len(self.sentence) - 2)]
        while len(s) != 0:
            i = 0
            while s[i].isalpha():
                i += 1
            l = s[0:i-1]
            j = i
            while s[j].is_number():
                j += 1
            n = float(s[(i + 1): j-1])
            c = Coordinates_tab(n, l).coordinates_to_int()
            R.list.add_incompability(tab, c)
            s = s[(j + 1):]
        tab.rule_list.append(R)


    def to_fweight_formula(self):
        s = self.sentence[2:(len(self.sentence) - 1)]
        i = 0
        while s[i].is_number():
            i += 1
        l = float(s[0:i-1])
        j = i + 1
        while s[j].is_alpha():
            j += 1
        m = s[i: (j-1)]
        k = j + 1
        while s[k].is_number():
            k += 1
        n = float(s[j:(k-1)])
        weight = Weight(l)
        c = Coordinates_tab(n, m).coordinates_to_int()
        f = FWeight(c, weight)
        return f

    def to_fnon_formula(self):
        s = self.sentence[4:(len(self.sentence) - 1)]
        i = 0
        while s[i].is_alpha():
            i += 1
        m = s[0: i-1]
        j = i + 1
        while s[j].is_number():
            j += 1
        n = float(s[i:j-1])
        c = Coordinates_tab(n, m).coordinates_to_int()
        f= FNon(c)
        return f

    def fsolve(self, tab, coordinates):
        if self.isFormulaWeight():
            self.to_fweight_formula().weight_solve(tab, coordinates)
        else:
            if self.isFormulaNon():
                self.to_fnon_formula().non_solve(tab, coordinates)
            else:
                pass
